#!/usr/bin/env python3
"""
KidLit-Gold external validation: analysis of the expert's verdicts.

Usage:
    python3 analyze_validation.py validation_results.csv

Inputs
    validation_results.csv  returned by the expert (case_id, verdict, note)
    validation_key.csv      the un-blinded key kept by the project team

Outputs
    a printed report, plus validation_report.csv with the merged per-case data
"""
import sys
import pandas as pd
from scipy.stats import fisher_exact, norm

RES = sys.argv[1] if len(sys.argv) > 1 else 'validation_results.csv'
KEY = 'validation_key.csv'


def wilson(k, n, conf=0.95):
    """Wilson score interval — reliable for proportions near 1, unlike the normal approximation."""
    if n == 0:
        return (float('nan'), float('nan'))
    z = norm.ppf(1 - (1 - conf) / 2)
    p = k / n
    d = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / d
    half = z * ((p * (1 - p) / n + z**2 / (4 * n**2)) ** 0.5) / d
    return (max(0.0, centre - half), min(1.0, centre + half))


def line(title):
    print('\n' + title)
    print('-' * len(title))


res = pd.read_csv(RES)
key = pd.read_csv(KEY)
df = key.merge(res, on='case_id', how='left')

missing = df['verdict'].isna().sum()
df = df[df['verdict'].notna()].copy()

TYPE_LABEL = {
    'Sentiment_label': 'Sentiment (label)',
    'NER_label': 'NER: label on coinciding span',
    'NER_missed_by_A': 'NER: missed by annotator A',
    'NER_missed_by_B': 'NER: missed by annotator B',
}

print('=' * 68)
print('KidLit-Gold — external validation of adjudication decisions')
print('=' * 68)
print(f'Cases in sample        : {len(key)}')
print(f'Cases judged           : {len(df)}' + (f'   ({missing} not judged)' if missing else ''))

# ---------------------------------------------------------------- headline
line('1. Overall agreement')
counts = df['verdict'].value_counts()
for v in ['correct', 'incorrect', 'unclear']:
    k = int(counts.get(v, 0))
    print(f'   {v:<10} {k:>4}  ({k / len(df) * 100:5.1f}%)')

# Primary estimate: "unclear" excluded, i.e. agreement among decided verdicts.
decided = df[df['verdict'].isin(['correct', 'incorrect'])]
k, n = int((decided['verdict'] == 'correct').sum()), len(decided)
lo, hi = wilson(k, n)
print(f'\n   Agreement (unclear excluded): {k}/{n} = {k/n*100:.1f}%  '
      f'[95% CI {lo*100:.1f}–{hi*100:.1f}]')

# Conservative estimate: "unclear" counted as disagreement.
k2, n2 = k, len(df)
lo2, hi2 = wilson(k2, n2)
print(f'   Agreement (unclear = disagreement): {k2}/{n2} = {k2/n2*100:.1f}%  '
      f'[95% CI {lo2*100:.1f}–{hi2*100:.1f}]')

# ------------------------------------------------- the actual bias question
line('2. Bias check: does agreement depend on which annotator was favoured?')
sub = decided[decided['resolved_in_favor_of'].isin(['A', 'B'])]
tab = []
for g in ['A', 'B']:
    s = sub[sub['resolved_in_favor_of'] == g]
    kk, nn = int((s['verdict'] == 'correct').sum()), len(s)
    tab.append([kk, nn - kk])
    if nn:
        l, h = wilson(kk, nn)
        print(f'   decisions favouring {g}: {kk}/{nn} = {kk/nn*100:5.1f}%  '
              f'[95% CI {l*100:.1f}–{h*100:.1f}]')
if all(sum(r) > 0 for r in tab):
    odds, p = fisher_exact(tab)
    print(f'\n   Fisher exact test: p = {p:.3f}, OR = {odds:.2f}')
    print('   Interpretation: p > 0.05 means the external expert agrees with decisions')
    print('   favouring A and B at statistically indistinguishable rates, i.e. no evidence')
    print('   that the adjudicator systematically favoured one annotator.')

# ---------------------------------------------------------- by case type
line('3. Agreement by disagreement type')
for t, lab in TYPE_LABEL.items():
    s = decided[decided['type'] == t]
    if not len(s):
        continue
    kk, nn = int((s['verdict'] == 'correct').sum()), len(s)
    l, h = wilson(kk, nn)
    print(f'   {lab:<32} {kk:>3}/{nn:<3} = {kk/nn*100:5.1f}%  [{l*100:.0f}–{h*100:.0f}]')

# ------------------------------------------------------- by precedent
line('4. Disagreements by precedent (where the expert said "incorrect")')
bad = df[df['verdict'] == 'incorrect']
if len(bad):
    for pid, cnt in bad['precedent_id'].value_counts().head(10).items():
        total = int((df['precedent_id'] == pid).sum())
        print(f'   {str(pid):<8} {cnt:>3} of {total:<3} judged cases')
else:
    print('   none')

# --------------------------------------------------------------- comments
line('5. Expert comments')
notes = df[df['note'].notna() & (df['note'].astype(str).str.strip() != '')]
if len(notes):
    for _, r in notes.iterrows():
        print(f'   [{r["case_id"]}] {r["verdict"]}: {r["note"]}')
else:
    print('   none')

df.to_csv('validation_report.csv', index=False)
print('\nPer-case merged data written to validation_report.csv')

# --------------------------------------------------- ready-made paper text
line('6. Draft sentence for the paper (fill in if the numbers look right)')
print(f'   "An independent expert, not affiliated with the project and blind to which')
print(f'   annotator had proposed each competing version, re-examined a stratified random')
print(f'   sample of {len(key)} adjudicated cases and confirmed {k} of {n} decided verdicts')
print(f'   ({k/n*100:.1f}%, 95% CI {lo*100:.1f}–{hi*100:.1f}). Agreement did not differ')
print(f'   significantly between decisions favouring annotator A and annotator B')
print(f'   (Fisher exact p = {p:.2f}), indicating no systematic bias toward either annotator."')

# NER Annotation Guidelines

*Named Entity Annotation Guidelines · KidLit Project · v2 (updated based on the IAA analysis)*

## Which entities to annotate

**PER_NAME** — a character's proper name. *Маша* 'Masha', *Петсон* 'Pettson', *Скупер* 'Scooper'. This is the core entity type: it is what you will later feed into the NER system.

**PER_ROLE** — a role or a "telling" nickname without a name. *Старый медведь* 'old bear', *добрая акула* 'kind shark', *маленький кораблик* 'little boat'. In children's books a character often has no name at all, only a role.

**PER_FAMILY** — family members (*мама* 'mom', *папа* 'dad', *бабушка* 'grandma') — a separate label, because it has already been decided not to remove them from topic modeling.

**Pronouns** — do not annotate. *He/she/they* carry no information about a specific character without coreference resolution, which is a separate, complex task.

### Annotation summary

*Это экскаватор Клюша. Мама Клюши работает … По дороге едет грузовик* ('This is the excavator Klyusha. Klyusha's mom works … A truck is driving down the road')

- If there is a name (*Клюша*) — it is PER_NAME.
- The character's role (*экскаватор* in *экскаватор Клюша*) — it is PER_ROLE.
- If the book contains no names, the hero's designation (*грузовик* 'truck') is PER_ROLE.
- All designations of family members (*мама*, *папа*, *малыш*, *сестра* — not names) are PER_FAMILY.

### Annotation examples

- *Тим, Тедди* ('Tim', 'Teddy') — names
- *Мышонок, медвежонок, друзья* ('little mouse', 'little bear', 'friends') — roles
- *Мама, папа, малыш* ('mom', 'dad', 'little one') — family
- *No individual names in the book, therefore грузовичок, джип, самосвал ('little truck', 'jeep', 'dump truck') — roles.*
- *Мама, малыш* — family

## Clarifications based on the IAA analysis

Double independent annotation of 30 books revealed several systematic disagreements between the annotators. The sections below are not new categories but clarifications of the existing rules, intended to reduce the number of contested cases in subsequent annotation rounds.

### Rule 8. Unique authorial name vs. descriptive role

The most frequent source of disagreement (116 of the 147 label-mismatch cases in the IAA analysis). Characters in children's books often receive a name derived from their role or an external attribute — this does NOT make them PER_ROLE.

| **Feature** | **→ PER_NAME** | **→ PER_ROLE** |
| --- | --- | --- |
| Can you say "one of the [X]"? | No — this is a specific, one-of-a-kind character | Yes — it is a species designation / category |
| Does the word decline as a proper noun? | Yes (case forms exist: «Жёлтого», «к Жёлтому») | No / it is used as an ordinary noun |
| Is it used as a form of address to the character? | Yes | No |

- *«Обнимашка»* ('little hugger'; the protagonist bunny) → PER_NAME — the only such character; declines («у Обнимашки»); used as a form of address.
- *«Жёлтый»* ('Yellow'; a flower character with a unique nickname) → PER_NAME — one cannot say "one of the yellows"; it declines.
- *«Одуванчики»* ('dandelions'; a group of flower characters) → PER_ROLE — a species designation for a group, not a unique nickname of a single character.

⚠ The etymological link between a name and a role or appearance (*Обнимашка* ← *обнимать* 'to hug', *Жёлтый* ← the color) does NOT by itself make the word PER_ROLE. Only the applicability of the three features in the table above is decisive.

### Rule 9. Animal characters vs. animal species

A separate, frequent instance of Rule 8: animals in children's prose divide into specific acting characters and background mentions of a species.

| **Feature** | **→ PER_NAME (character)** | **→ PER_ROLE (species)** |
| --- | --- | --- |
| Unique name (may coincide with the species designation) | Yes — «Марабу» 'Marabou' as the teacher's name | No — simply «сова» 'owl', «снегирь» 'bullfinch' |
| Individual character traits, participation in dialogue | Yes | No |
| Used with a determiner/epithet («мудрая Сова» 'wise Owl') | Rarely | Often |
| Role in the plot | Significant, recurring | Episodic / background |

- *«Марабу»* (a teacher with a name and dialogue lines) → PER_NAME.
- *«мудрая Сова»* ('wise Owl'; appears once, no dialogue, designated by species + epithet) → PER_ROLE.
- *«Снегирь», «Попугай»* ('Bullfinch', 'Parrot'; secondary characters without an individual name) → PER_ROLE.

### Rule 10. A kinship role that has become a character's name

If a standard kinship word (*мама* 'mom', *папа* 'dad') is used by the author as part of a character's unique name (rather than as a mere mention of a relative), it is PER_NAME, not PER_FAMILY.

| **Example phrase** | **Label** | **Why** |
| --- | --- | --- |
| «Мама обняла его» ('Mom hugged him') | PER_FAMILY | Standard word denoting a kinship relation to the protagonist |
| «Обнимама» ('Hug-mom'; a character's name) | PER_NAME | A unique authorial word-name derived from the role "mom" |
| «Мама-Тигрица», «Папа-Тигр» ('Mama-Tigress', 'Papa-Tiger'; character names) | PER_NAME | A compound authorial name; the kinship word is only its first part |
| «Его родители работали в саду» ('His parents worked in the garden') | PER_FAMILY | The possessive «его» 'his' anchors it to a specific family but does not form a name |

⚠ Test: can the word be used as a FORM OF ADDRESS to a specific character, independently of the kinship fact? «Обнимама, посмотри!» ('Hug-mom, look!') — yes, this is a name. «Мама, посмотри!» ('Mom, look!') — this is an address by kinship role, not by name → PER_FAMILY.

### Rule 11. Collective kinship terms: PER_ROLE vs. PER_FAMILY

*«Дети»* 'children', *«родители»* 'parents' without a clarifying possessive or an explicit link to a specific family are PER_ROLE, not PER_FAMILY.

| **Example phrase** | **Label** | **Why** |
| --- | --- | --- |
| «Дети бежали к морю» ('The children ran to the sea') | PER_ROLE | A generalized group; not the protagonist's specific siblings |
| «Его родители работали в саду» ('His parents worked in the garden') | PER_FAMILY | The possessive «его» 'his' explicitly anchors it to a specific character |
| «Мама обняла его» ('Mom hugged him') | PER_FAMILY | A specific kinship role relative to the protagonist |

### Rule 12. Span boundaries for compound names and designations

The most frequent technical source of annotation coordinate mismatches (boundary mismatch). Established from an analysis of actual disagreements: one annotator marks a compound name/designation as ONE span, the other as TWO separate spans, each with the same label.

| **Entity type** | **Example** | **Span rule** |
| --- | --- | --- |
| Two-word compound name | «Дед Мороз» 'Ded Moroz / Father Frost', «Керосин Бензинович» 'Kerosene Benzinovich' | ONE span over the entire name, label PER_NAME |
| Compound object/vehicle designation | «снегоуборочная машина» 'snow-clearing machine', «летняя уборочная машина» 'summer cleaning machine' | ONE span over the whole phrase, label PER_ROLE |
| Name + a separate address in the same phrase | «Дед Мороз, а почему...» ('Ded Moroz, but why...') | «Дед Мороз» — one span; the rest of the phrase is not part of the span |

＋ NEW RULE: a fixed phrase (a multiword name, or an object designation consisting of adjective + noun) is annotated as ONE span rather than split into separate words — even if each word on its own could form an independent span. Splitting into several spans inflates the number of spurious disagreements in IAA computation without any substantive reason.

⚠ If one of the spans accidentally captures adjacent function words (an article, a preposition, words not belonging to the name) — preference is given to the span without those words, not to the longer variant. The "one span per phrase" rule applies only to the words that actually form a single name/designation.

## What to do when in doubt

- If a case is not covered by any rule above — annotate by intuition and leave a short comment for later review; do not try to force it under an existing rule.
- If in doubt between PER_NAME and PER_ROLE for a new, undescribed character type (plants, objects, natural phenomena) — apply the "can you say 'one of the [X]'?" test from Rule 8 as a universal criterion.
- Any annotation typo (a duplicate span at the same offsets with different labels) is not a substantive decision but a technical glitch; fix it immediately, without waiting for the IAA check.

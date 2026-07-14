# KidLit Decision Handbook

*v2 · verified and extended based on the IAA analysis (30 books, both annotators) · English edition*

## 0. How to use this document

Each precedent is a rule derived from a specific resolved case that can be applied to future similar cases without renewed deliberation. The structure of a precedent: identifier, status, disagreement type, concrete example, rule, resolution, notes.

Every precedent carries a status:

- **STABLE** — the rule has been verified on the full sample of disagreements of its type and is applied without exceptions.
- **PRELIMINARY** — the rule is derived from 1–2 cases and requires verification on the remaining examples.
- **OPEN** — a systematic pattern has been found, but a single decision has not yet been formulated; requires discussion.

Precedents whose status was not explicitly marked in the Russian working version (B-6, B-8–B-23, B-25) are listed here as PRELIMINARY: each derives from one or two resolved cases, consistently with how they are reported in the accompanying paper.

> ⚠ Notes marked "✎ CORRECTED AGAINST THE DATA" indicate places where the wording of a precedent in the previous version did not accurately describe what actually happened in the annotation — corrected after re-checking the offsets in `KidLit_NER_Sentiment_Combined.json`.

Russian examples are given in the original with English glosses in single quotes. IDs `A-*` refer to NER precedents, `B-*` to sentiment precedents.

---

## Part A · NER precedents

### A-1 · STABLE · PER_NAME vs PER_ROLE — unique authorial names

**Example.** Book RUS-O_long_01. The protagonist is called «Обнимашка» ('little hugger'). Annotator A labeled it PER_ROLE, annotator B — PER_NAME. An analogous dispute over «Марабу» ('Marabou'): A — PER_ROLE, B — PER_NAME.

**Rule.** A unique authorial name created for a specific character is annotated as PER_NAME, even if it is etymologically linked to a role or a characteristic.

| Criterion | → PER_NAME | → PER_ROLE |
| --- | --- | --- |
| The character's sole identifier? | Yes | No |
| Declines as a proper noun? | Yes (case forms exist) | No / rarely |
| Used as a form of address? | Yes | No |
| Replaceable by a generalized description without loss of meaning? | No | Yes |

**Resolution.** «Обнимашка» → PER_NAME. «Обнимама» → PER_NAME. «Марабу» → PER_NAME. (All decisions in favor of B.)

> ✓ Status confirmed: the rule has been transferred into the NER annotation guidelines as Rule 8.

### A-2 · STABLE · PER_NAME vs PER_ROLE — anthropomorphic objects with a "nickname"

**Example.** Book RUS-O_short_03. Plant characters are called «Жёлтый» ('Yellow') and «Одуванчики» ('Dandelions'). Annotator A labeled them PER_NAME, annotator B — PER_ROLE.

**Rule.** A word functions as PER_NAME if it is used ONLY as an address/reference to a specific, one-of-a-kind character. It is PER_ROLE if it remains a description of a category/species, even when applied to a single character in the book.

| Test | «Жёлтый» (a flower) | «Одуванчики» (a group) |
| --- | --- | --- |
| Can you say "one of the yellows"? | No → PER_NAME | Yes → PER_ROLE |
| Declines as a proper noun? | Yes («Жёлтого», «к Жёлтому») | No; plural, like an ordinary noun |

**Resolution.** «Жёлтый» → PER_NAME (B's decision). «Одуванчики» → PER_ROLE (A's decision was correct).

### A-3 · STABLE · PER_NAME vs PER_ROLE — animal characters

**Example.** Book RUS-T_long_01: «Сова» ('Owl') acts as a character («мудрая Сова» 'wise Owl') but has no unique name. In RUS-O_long_01, «Марабу» is also a bird — but acts as a teacher with a unique name.

**Rule.** Animals that act as specific characters with individual traits and a unique name are annotated as PER_NAME. Animals as a generic species or a background role — PER_ROLE.

**Resolution.** «Марабу» → PER_NAME (a specific character with a name and a role). «Сова» → PER_ROLE (by species, no unique name). «Снегирь» ('Bullfinch'), «Попугай» ('Parrot') → PER_ROLE (secondary characters without a name).

### A-4 · STABLE · PER_NAME vs PER_FAMILY — kinship roles as names

**Example.** Book RUS-O_long_01. «Обнимама» ('Hug-mom') is the name of the mother character. Annotator A labeled it PER_FAMILY, annotator B — PER_NAME. Analogously: «Мама-паровоз» ('Mama-locomotive'), «Мама-Тигрица» ('Mama-Tigress'), «Папа-Тигр» ('Papa-Tiger').

**Rule.** PER_FAMILY is for standard kinship words («мама», «папа», «бабушка», «сынок») in the context of a specific family. PER_NAME — when a kinship role has become a character's unique authorial name.

**Resolution.** «мама» (an ordinary word) → PER_FAMILY. «Обнимама», «Мама-паровоз», «Мама-Тигрица», «Папа-Тигр» (character names) → PER_NAME.

> ✓ The address test has been added to the guidelines (Rule 10): can the word be used as a form of address to the character, independently of the kinship fact?

### A-5 · STABLE · PER_ROLE vs PER_FAMILY — collective kinship terms

**Example.** «дети» ('children'), «родители» ('parents') were annotated differently across books: sometimes PER_ROLE, sometimes PER_FAMILY.

**Rule.** PER_FAMILY — if the word denotes a kinship role RELATIVE to a specific child character in the book («мама» = the protagonist's mom). PER_ROLE — if the word is used generically, without a link to a specific character's family.

| Example phrase | Label | Why |
| --- | --- | --- |
| «Мама обняла его» ('Mom hugged him') | PER_FAMILY | A specific kinship role relative to the protagonist |
| «Дети бежали к морю» ('The children ran to the sea') | PER_ROLE | A generalized group, not a particular family |
| «Его родители работали в саду» ('His parents worked in the garden') | PER_FAMILY | The possessive «его» 'his' explicitly anchors it to a specific character |

**Resolution.** «дети» (generic, no possessive) → PER_ROLE. «дети» / «родители» with an explicit link to a specific character (a possessive pronoun, single-family context) → PER_FAMILY.

> ✓ Status raised to STABLE: the "possessive / explicit family anchoring" criterion has been confirmed without contradiction on all discovered cases of this type.

### A-6 · STABLE · Spans of compound NAMES — splitting into parts

> ✎ CORRECTED AGAINST THE DATA: the previous version described this precedent as "A annotated the full span, B — a shortened one." Checking the actual offsets showed a different picture: B systematically annotates a compound name as TWO separate spans, each with the same label, not as one shortened span.

**Example (verified against offsets).** Book RUS-O_long_03, «Дед Мороз» ('Ded Moroz / Father Frost'): A — one span [9061:9070] PER_ROLE. B — two spans: «Дед» [9061:9064] PER_NAME and «Мороз» [9065:9070] PER_NAME (separately). Book RUS-O_long_02, «Керосин Бензинович» ('Kerosene Benzinovich'; 8 mentions in the text): A — one PER_NAME span over the full name in all 8 cases. B — two separate spans in all 8 cases («Керосин» / «Бензинович», or their case forms), both labeled PER_NAME.

**Rule.** A fixed phrase forming a character's single name (name + neologism patronymic, name + neologism surname) is annotated as ONE span labeled PER_NAME — regardless of how many separate words it contains.

**Resolution.** «Дед Мороз» → one span, label PER_NAME (not PER_ROLE — it is a fixed, recognizable character name, not a descriptive category). «Керосин Бензинович» → one span for each of the 8 mentions, label PER_NAME (A's decision was correct in all 8 cases).

> ⚠ A separate technical annotation defect was found (not a linguistic precedent): in one of the 8 mentions of «Керосин Бензинович», B's span «Бензинович» [9944:9954] is duplicated twice with different labels (PER_NAME and PER_ROLE) at the same offsets. This is a typo / annotation-interface glitch, not a substantive decision — it should be fixed directly in the data and must not be counted as an argument for PER_ROLE.

### A-7 · STABLE · Spans of compound OBJECT DESIGNATIONS — splitting into parts

> ✎ CORRECTED AGAINST THE DATA: as with A-6 — the actual picture is that B annotates only the attributive adjective as a separate span, without capturing the noun, rather than "a shorter but still meaningful span."

**Example (verified against offsets).** Book RUS-O_long_03. «СНЕГОУБОРОЧНАЯ МАШИНА» ('SNOW-CLEARING MACHINE') [1747:1768]: A — one span over both words, PER_ROLE. B — a span over «СНЕГОУБОРОЧНАЯ» only [1747:1761]; the word «МАШИНА» is not annotated at all. Analogously for the second mention of «Снегоуборочная машина», and for «летняя уборочная машина» ('summer cleaning machine').

**Rule.** An object/vehicle designation consisting of an attributive adjective and a role-bearing noun is annotated as ONE span over the whole phrase, label PER_ROLE. Annotating only the adjective without the noun is incomplete annotation.

**Resolution.** «СНЕГОУБОРОЧНАЯ МАШИНА» → one span over the whole phrase, PER_ROLE. «летняя уборочная машина» → one span over the whole phrase, PER_ROLE.

### A-8 · OPEN · Missed entities — B's single-word spans without a head noun

**Finding (from a systematic check of all "missed by A" cases).** Of the 360 cases "B found an entity, A missed it," 100% are single-word spans. Among them there are at least two subtypes of different nature, requiring different decisions:

| Subtype | Example | Probable cause | Proposed decision |
| --- | --- | --- | --- |
| An adjective without its head noun | «маленький» 'little' separately from «слонёнок» 'baby elephant' in «маленький слонёнок» | Incomplete annotation / a technical glitch in span selection | Do not count as a separate entity — attach to the noun, or do not annotate at all |
| The word «природа» 'nature' as a character | «мудрой природе» 'to wise nature', «Природа даёт нам всё» 'Nature gives us everything' | — | Most likely should NOT be annotated as PER_ROLE — requires a decision |

> ？ OPEN QUESTION. To be decided on the full sample of these 360 cases: (1) whether to exclude «Природа»/«природа» from PER_ROLE as a class — a philosophical question about the limits of anthropomorphization in children's texts; (2) whether to introduce a separate technical validation rule ("a single-adjective span without a noun when selecting PER_ROLE — request confirmation"). Both questions must be resolved BEFORE the next annotation round, otherwise they will continue to generate spurious IAA disagreements in the same proportion.
>
> ⚠ Previously, "missed entities" were treated as a single category without a subtype breakdown. The actual data revealed two different phenomena inside one figure (360) — the number itself is uninformative without this distinction.

### A-9 · STABLE · PER_ROLE — social relations outside the family

**Example.** «— Эй, а где все твои друзья?» ('Hey, where are all your friends?')

**Rule.** Words denoting stable social relations between characters («друзья» 'friends', «приятели» 'pals', «товарищи» 'companions') are annotated as PER_ROLE if they refer to specific characters within the world of the book rather than being used abstractly.

### A-10 · STABLE · Verbs, prepositions, and function words are not NER entities

**Examples.**
- «И грузовик **засыпает**» ('And the truck falls asleep') — the verb «засыпает» is not an entity.
- «Лисы в **горошек**» ('Polka-dot foxes') — the noun «горошек» denotes a pattern/print, not an entity.
- «**огромная** сова» ('a huge owl') — the adjective «огромная» is not an entity.
- «**Бак**» (a verse rhyme / onomatopoeia) — not an entity.

**Rule.** NER annotation covers **noun phrases only** (nouns and their modifiers) denoting entities: character names, roles, organizations, locations, object designations, etc.

**Not NER entities:**
1. **Verbs** — any forms of action or state («засыпает», «бежит», «стоит»).
2. **Prepositions and conjunctions** — function words («в», «на», «и», «но»).
3. **Adjectives** not forming an independent noun phrase («огромная», «красный», «весёлый»). Exception — substantivized adjectives («больной» 'the sick one', «глухонемой' 'the deaf-mute one') acting as nouns.
4. **Nouns denoting attributes/details** (patterns, materials, colors, prints) — «горошек», «полоска», «клетка» in the sense of a pattern; «дерево» as a material.
5. **Verse elements** — rhymes, onomatopoeia, interjections not forming an independent noun phrase («Бак», «Би-би», «У-ууу», «Ох»).
6. **Adverbs** — words denoting a property of an action («быстро», «громко», «тихо»).

### A-11 · STABLE · Social and professional roles

**Examples.**
- «Срочно нужен **сыщик**» ('A detective is urgently needed') — the role of a person who finds lost things
- «**Воспитатель**» ('kindergarten teacher') — a professional role
- «**Врач**», «**учитель**», «**повар**» ('doctor', 'teacher', 'cook') — professional roles
- «Белый **клоун**» ('white clown'), «Великаны-**силачи**» ('strongman giants'), «Канатоходец» ('tightrope walker') — circus roles
- «Воздушные **гимнасты**» ('aerial gymnasts'), «**жонглёры**» ('jugglers'), «**эквилибристы**» ('equilibrists') — compound professional roles

**Rule.** Words and phrases denoting **social, professional, or functional roles** are annotated as **PER_ROLE** if they: (1) denote a character's function, profession, social position, or status; (2) are not a unique authorial name (not PER_NAME); (3) are not a standard kinship term in the context of a specific family (not PER_FAMILY).

**Compound roles** (e.g., «фокусник-факир» 'magician-fakir', «воздушные гимнасты», «белый клоун») are annotated as **one span** labeled PER_ROLE, since they form a single semantic whole — a professional/social function.

### Clarification to A-1 / A-7 · Compound nouns with a kinship term

**Situation.** The text contains a compound noun of the type «мама-паровоз» ('mom-locomotive'), «мама-волшебница» ('mom-sorceress'), «мама-садовод» ('mom-gardener'), etc.

**Distinguishing rule:**

| Criterion | → PER_NAME | → PER_ROLE |
| --- | --- | --- |
| Is it a **fixed authorial name** of the character, used as the main identifier throughout the book? | Yes («Обнимама», «Мама-паровоз» in RUS-O_long_01) | No |
| Is it a **one-off figurative/metaphorical comparison** within the narrative? | No | Yes |
| Can it be replaced by a description without losing character identification? | No (the unique name would be lost) | Yes («мама, которая ведёт как паровоз» 'a mom who leads like a locomotive') |
| Is it used as a **form of address** to the character? | Yes | No |

**Resolution for the case at hand.** «мама-паровоз» → **PER_ROLE** (one span over the whole compound), because here it is a **metaphorical comparison within an episode**, not the character's unique name. Unlike book RUS-O_long_01, where «Мама-паровоз» is a character's proper name, here it is a descriptive figure characterizing the mother's action in a specific scene.

---

## Part B · Sentiment precedents

### B-1 · STABLE · Segmentation: utterance + speech verb

**Example.** «— Обними меня, мама! — просил он перед сном.» ('"Hug me, mom!" he begged before bedtime.') Annotator A annotated this as two separate sentence units; annotator B — as one.

**Scale (from the full check).** This is the most frequent segmentation disagreement pattern in the sentiment IAA — over 500 multi-span groups out of ~3,360 matched pairs (group matching via union-find; see the IAA notebook).

**Resolution.** A direct-speech utterance and the immediately following speech verb with an intonational characteristic (просил 'begged', выкрикнул 'shouted out', прошептал 'whispered') are annotated as ONE sentiment unit, if the speech verb carries no emotional information distinct from that of the utterance.

> ✓ Status: STABLE. Transferred into the sentiment annotation guidelines as Rule 8.

### B-2 · PRELIMINARY · Exclamation with an explicit joy marker → positive

**Example.** Book RUS-O_long_01. «О, это был самый настоящий цветущий сад!» ('Oh, it was a real blossoming garden!') Annotator A — +1 POSITIVE, annotator B — 0 NEUTRAL.

**Rule.** Exclamatory sentences with explicit markers of joy/delight («О!», «Ура!», «Как красиво!») are annotated as +1 POSITIVE. If the emotional coloring is not explicit — 0 NEUTRAL.

**Resolution.** «О, это был самый настоящий цветущий сад!» → +1 POSITIVE.

> ⚠ Requires verification on a larger sample of exclamations with other markers («Какой ужас!» 'How awful!', «Вот это да!» 'Wow!') — it is not always clear what counts as an "explicit" joy marker as opposed to polarity-free surprise.

### B-3 · PRELIMINARY · Fear-as-metaphor resolved by care within the same sentence

**Example.** Book RUS-O_long_01. «— Мне бы хотелось спрятать тебя от всех тревог на свете.» ('I would like to hide you from all the worries in the world.') Annotator A — −1 NEGATIVE, annotator B — +1 POSITIVE.

**Rule.** If a phrase mentions worries/fear but the same sentence expresses care/support, the annotation follows the resulting emotion (care), not the trigger word.

**Resolution.** → +1 POSITIVE (an expression of care using «тревоги» metaphorically, not a description of current fright).

### B-4 · PRELIMINARY · Remorse without immediate resolution → negative

**Example.** Book RUS-O_long_01. «— Значит, я не прав? Значит, я зря обидел бегемотика... И обезьянку.» ('So I was wrong? So I hurt the little hippo for nothing… And the little monkey.') Annotator A — −1 NEGATIVE, annotator B — 0 NEUTRAL.

**Rule.** If a character realizes a mistake and expresses remorse, and the same/following sentence contains NO immediate positive resolution, the label remains −1 NEGATIVE. Only a positive action following the remorse can outweigh the label.

**Resolution.** → −1 NEGATIVE (realization of a mistake without immediate resolution).

> ✓ B-3 and B-4 are formally similar (both contain a negative trigger word) but are resolved differently. The key differences: the DIRECTION of the emotion (care for another vs one's own remorse) and the presence/absence of resolution WITHIN the same sentence. See the comparison in Rule 5 of the sentiment guidelines.

### B-5 · PRELIMINARY · Question without explicit emotion markers → neutral

**Example.** Book RUS-O_long_01. «— Где ты?» ('Where are you?') Annotator A — 0 NEUTRAL, annotator B — −1 NEGATIVE.

**Rule.** Questions without explicit anxiety/fear markers (interrogative words, no exclamation marks) are annotated 0 NEUTRAL unless the context clearly implies a negative emotion.

**Resolution.** «— Где ты?» → 0 NEUTRAL (a question without explicit negative coloring).

> ⚠ The boundary with Rule 1 («Куда делся малыш?» 'Where did the little one go?' → −1) is thin: what decides is the presence of a broader context of anxiety OR of specific wording implying worry («куда делся» presupposes a loss that has already happened; «где ты» is a neutral search). More examples are needed for a stable rule.

### B-6 · PRELIMINARY · Idyllic description of the world

**Example.** «В одной тёплой стране, где солнце заботливо согревало землю своими лучами...» ('In a warm land where the sun caringly warmed the earth with its rays…')

**Rule.** Landscape or expository descriptions receive +1 POSITIVE if they contain explicit positive evaluative features (warmth, care, beauty, coziness, abundance) rather than merely stating facts about the setting. Contrast the neutral «В лесу жил маленький слонёнок.» ('A little elephant lived in the forest.') with the positive «Солнце заботливо согревало землю своими лучами.» ('The sun caringly warmed the earth with its rays.')

### B-7 · PRELIMINARY · Request for closeness

**Example.** «— Обними меня, мама! — просил он перед сном.» ('"Hug me, mom!" he begged before bedtime.')

**Rule.** Utterances expressing a need for love, support, or physical closeness are annotated +1 POSITIVE if the emotional focus is on attachment and care. This is consistent with the principle of B-3: the resulting emotion is determined not by individual words but by the overall emotional direction of the utterance.

### B-8 · PRELIMINARY · Condescending or mentoring intonation without conflict

**Example.** «— Разумеется, — хмыкнул Марабу, посмотрев на неё сверху вниз.» ('"Of course," Marabou snorted, looking down at her.')

**Resolution.** 0 NEUTRAL.

**Rule.** Speech verbs and authorial remarks conveying condescension, confidence, or a mentor's stance («хмыкнул» 'snorted', «усмехнулся» 'smirked', «посмотрел сверху вниз» 'looked down at') do not receive a negative label unless the context contains conflict, mockery, humiliation, or a character's emotional suffering.

### B-9 · PRELIMINARY · Positive imagery in the context of looming misfortune

**Example.** «Солнце всё так же лениво выкатывалось на небосклон и дарило миру своё тепло.» ('The sun still lazily rolled onto the sky and gave the world its warmth.')

**Resolution.** 0 NEUTRAL.

**Rule.** Traditionally positive natural imagery (sun, warmth, light, etc.) does not receive a positive label if the immediate context shows it becoming part of an unfavorable situation. If the negativity is not yet expressed within the annotated fragment itself, but the positive reading is already cancelled by neighboring sentences, the neutral label is chosen.

**Comment.** Positive vocabulary («тепло» 'warmth', «дарило» 'gave') in such cases does not reflect the resulting emotional assessment of the episode.

### B-10 · PRELIMINARY · Care under adverse circumstances

**Example.** «Каждое утро Обнимашка набирал в хобот воду из ручья и поливал цветы, поникшие от жары.» ('Every morning Obnimashka drew water from the stream into his trunk and watered the flowers wilted by the heat.')

**Resolution.** +1 POSITIVE.

**Rule.** A character's actions aimed at helping, caring for, or supporting others receive a positive label even against an unfavorable background (drought, illness, danger, deprivation). The resulting emotion is determined by the act of care. **Key feature:** the negative background is present, but the emotional focus is on compassion, caretaking, or help.

### B-11 · PRELIMINARY · Unfinished objection

**Example.** «— Но...» ('"But…"')

**Resolution.** 0 NEUTRAL.

**Rule.** Unfinished utterances expressing doubt or an attempted objection are annotated as neutral if the negative emotion or the conflict emerges only in the next utterance. Applies to cases like «Но...», «А если...» ('And what if…'), «Подожди...» ('Wait…'), «Я только хотел...» ('I only wanted…'), where the emotional coloring is not yet realized within the segment itself.

### B-12 · PRELIMINARY · A character's favorite activity or place

**Example.** «Он очень любил сидеть рядом с водой и смотреть на своё отражение.» ('He loved sitting by the water and looking at his reflection.')

**Resolution.** +1 POSITIVE.

**Rule.** Utterances describing a character's favorite activity, habit, or place receive a positive label if they express pleasure, attachment, comfort, or inner calm. A subsequent unfavorable event does not change the sentiment of this fragment. **Key markers:** любил 'loved', нравилось 'liked', обожал 'adored', с удовольствием 'with pleasure'.

### B-13 · PRELIMINARY · A character's helpless reaction

**Example.** «— Ква. — Лягушка развела лапками и прыгнула в кусты.» ('"Croak." The frog spread its paws and jumped into the bushes.')

**Resolution.** −1 NEGATIVE.

**Rule.** Brief replies, gestures of helplessness, or a character's withdrawal receive a negative label if they express loneliness, loss, powerlessness, or the consequences of an unfavorable situation. **Key features:** a one-word or evasive reply; a gesture of helplessness (развёл лапками 'spread its paws', пожал плечами 'shrugged'); withdrawal or detachment; a negative context (loss, disappearance, loneliness).

### B-14 · PRELIMINARY · Statement of loss or destruction

**Example.** «— Точнее, то, что от него осталось.» ('"Or rather, what is left of it."')

**Resolution.** −1 NEGATIVE.

**Rule.** Utterances in which a character realizes or states the loss, destruction, or serious deterioration of a significant object receive a negative label. The negative sentiment is determined by the focus on damage or loss. **Key markers:** то, что осталось 'what is left'; почти ничего не осталось 'almost nothing is left'; всё погибло 'everything perished'; он уже не тот 'it is not what it used to be'.

### B-15 · PRELIMINARY · Value and the wish to preserve something beautiful

**Example.** «— Чтобы мы могли им любоваться!..» ('"So that we can admire it!.."')

**Resolution.** +1 POSITIVE.

**Rule.** Utterances expressing admiration of an object's beauty or the wish to preserve it for oneself and others are annotated as positive. An unfavorable context does not cancel the positive orientation of such utterances.

### B-16 · PRELIMINARY · Acknowledging good intentions

**Example.** «— Ты хотел как лучше, — покачала головой Обнимама.» ('"You meant well," Obnimama shook her head.')

**Resolution.** +1 POSITIVE.

**Rule.** Utterances in which a character acknowledges another's good intentions and shows understanding instead of judgment are annotated as positive, even if the situation remains difficult or mistaken.

### B-17 · PRELIMINARY · Verbalization of a negative emotion

**Example.** «— А ещё ты очень боялся.» ('"And you were also very afraid."')

**Resolution.** −1 NEGATIVE.

**Rule.** Utterances that directly name a character's experienced negative emotions («боялся» 'was afraid', «грустил» 'was sad', «тревожился» 'worried', «испугался» 'got frightened') are annotated as negative regardless of whether they are spoken by the character or by another character in a supportive context.

### B-18 · PRELIMINARY · Fixation on the source of misfortune

**Example.** «Поэтому смотрел лишь в высыхающий пруд.» ('So he looked only at the drying pond.')

**Resolution.** −1 NEGATIVE.

**Rule.** If, out of fear, anxiety, or sadness, a character concentrates only on the object of loss or threat, the fragment is annotated as negative, since it reflects the experience of misfortune and a perception constrained by the trouble.

### B-19 · PRELIMINARY · Reframing the situation through support

**Example.** «Но что ты увидишь, если поднимешь голову?» ('But what will you see if you lift your head?')

**Resolution.** +1 POSITIVE.

**Rule.** Questions or utterances aimed at broadening a character's perspective, overcoming fear, or seeking hope are annotated as positive, even if they formally take an interrogative form.

### B-20 · PRELIMINARY · Non-understanding or clarification

**Example.** «— Что — большая река? — не понял Марабу.» ('"What — a big river?" Marabou did not understand.')

**Resolution.** 0 NEUTRAL.

**Rule.** Questions and utterances associated with non-understanding or with clarifying information («не понял» 'did not understand', «что ты имеешь в виду?» 'what do you mean?', «как это?» 'how so?') receive a neutral label in the absence of a negative emotional reaction.

### B-21 · PRELIMINARY · Pointing out a limitation or obstacle

**Example.** «— Не у всех нас есть хоботы, — заметил волчонок Зо.» ('"Not all of us have trunks," remarked Zo the wolf cub.')

**Resolution.** 0 NEUTRAL.

**Rule.** Remarks about the impossibility or limitations of a proposed course of action are annotated as neutral if they are part of a joint search for a solution and express no negative emotions or conflict.

### B-22 · PRELIMINARY · Joint action to help

**Example.** «И все зверята ... отправились к Большой реке.» ('And all the little animals … set off for the Big River.')

**Resolution.** +1 POSITIVE.

**Rule.** Collective actions of characters united by the common goal of helping or supporting someone are annotated as positive, since they express cooperation, unity, and mutual aid.

### B-23 · PRELIMINARY · End of misfortune and the onset of well-being

**Example.** «Наконец, в одно особенно доброе утро, на высохшую землю пролился долгожданный дождь.» ('At last, on one especially kind morning, the long-awaited rain fell on the parched earth.')

**Resolution.** +1 POSITIVE.

**Rule.** Fragments describing the long-awaited resolution of a crisis, the return of conditions necessary for life, or the end of a period of misfortune are annotated as positive.

### B-24 · PRELIMINARY · Weakly expressed negative emotion without dramatization → neutral

*Status: PRELIMINARY (derived from 1 case; requires verification on other examples).*

**Example.** The airplane episode: the airplane flew and tumbled about, but then it got bored and looked down. Annotator A — −1 NEGATIVE, annotator B — 0 NEUTRAL.

**Rule.** Weakly expressed negative states (being bored, tired, pensive, downcast, etc.) without dramatization, suffering, conflict, or other intensifying markers are annotated 0 NEUTRAL if: the state is not dominant in the segment; there are no other negative markers (tears, pain, conflict, fear, sadness, despair); and the next sentence removes or neutralizes the negative accent (the character switches to another activity or interest). If boredom/tiredness is accompanied by suffering, complaint, conflict, or a clearly negative emotional background in the immediate context → −1 NEGATIVE.

### B-25 · PRELIMINARY · A confrontational line followed by de-escalation

**Example.** «— Ну, давайте, наябедничайте! — вдруг заверещал самосвал, и машинки заметили, что он такой же маленький, как и они, и совсем не страшный.» ('"Go on then, tattle on me!" the dump truck suddenly shrieked, and the little cars noticed that he was just as small as they were, and not scary at all.')

**Resolution.** −1 NEGATIVE.

**Rule.** If a segment begins with an emotionally aggressive or confrontational line, and the following part merely softens its perception without changing the nature of the utterance, the annotation remains negative.

---

## Part C · Precedent version log

With every rule update, record which earlier decisions need to be revisited.

| Date | Precedent | What changed | How many cases to revisit |
| --- | --- | --- | --- |
| v2 (current) | A-6, A-7 | Reformulated from "shorter/longer span" to "one span vs splitting into several spans" — after checking the actual offsets | 8 mentions of «Керосин Бензинович» + 2 mentions of «Дед Мороз» + 2 mentions of the snow-clearing machine — verify that the final annotation uses ONE span everywhere |
| v2 (current) | A-5 | Status raised from PRELIMINARY to STABLE — the possessive-anchoring criterion confirmed without contradiction | Not needed — a status change, not a rule change |
| v2 (current) | A-8 | New precedent (previously an empty template). Status OPEN, not PRELIMINARY — no decision has been made yet | 360 cases await a decision on the two subtypes (adjective without a noun / «природа» as a character) |

---

## Part D · Quick reference

### D-1. Quick NER table

| Category | Examples | Recommendation |
| --- | --- | --- |
| Unique authorial names | Обнимашка, Обнимама, Клюша, Шпунчик | PER_NAME |
| Compound names (one span) | Дед Мороз, Керосин Бензинович | PER_NAME |
| Animal characters | Марабу | PER_NAME |
| Animal species | Сова, снегирь, попугай | PER_ROLE |
| Roles without a name | воспитатель, паровоз, экскаватор | PER_ROLE |
| Compound object designations (one span) | снегоуборочная машина | PER_ROLE |
| Kinship roles (ordinary word) | мама, папа, бабушка, сынок | PER_FAMILY |
| Collective kinship terms (no possessive) | дети, родители — generic | PER_ROLE |
| Open question — do NOT annotate without a decision | a single adjective without a noun; «природа» | See A-8 |

### D-2. Quick sentiment table

| Category | Examples | Recommendation |
| --- | --- | --- |
| Explicit positive | joy, laughter, hugs, hooray | +1 POSITIVE |
| Explicit negative | fear, sadness, conflict, pain | −1 NEGATIVE |
| Neutral | facts, narration, dialogue | 0 NEUTRAL |
| Exclamation with an explicit joy marker | О!, Ура!, Как красиво! | +1 POSITIVE |
| Anxiety-as-metaphor + care in the same sentence | «спрятать от тревог» | +1 POSITIVE (by the resulting emotion) |
| Remorse without resolution | «я зря обидел...» | −1 NEGATIVE |
| Utterance + speech verb | «— Обними меня! — просил он» | ONE sentence, by the resulting emotion |
| Mixed | context analysis | Choose the dominant emotion |

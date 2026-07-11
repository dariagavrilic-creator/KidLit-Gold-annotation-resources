# NER Annotation Guidelines

*KidLit Project*

## Which entities to annotate

**PER_NAME** — a character's proper name. *Маша* 'Masha', *Петсон* 'Pettson', *Тим* 'Tim'. 

**PER_ROLE** — a role or a "telling" nickname without a name. *Медвежонок* 'little bear', *добрая акула* 'kind shark', *грузовик* 'truck'. 

**PER_FAMILY** — family members *мама* 'mom', *папа* 'dad', *бабушка* 'grandma'.

**Pronouns** — do not annotate. *He/she/they* carry no information about a specific character.

### Annotation summary

*Это экскаватор Клюша. Мама Клюши работает … По дороге едет грузовик* ('This is the excavator Klyusha. Klyusha's mom works … A truck is driving down the road')

- If there is a name (*Клюша* 'Klyusha') — it is PER_NAME.
- The character's role (*экскаватор* 'excavator' in *экскаватор Клюша* 'excavator Klyusha') — it is PER_ROLE.
- If the book contains no names, the hero's designation (*грузовик* 'truck') is PER_ROLE.
- All designations of family members (*мама*, *папа*, *малыш*, *сестра* — not names) are PER_FAMILY.

### Annotation examples

- *Тим, Тедди* ('Tim', 'Teddy') — names
- *Мышонок, медвежонок, грузовичок, джип, самосвал* ('little mouse', 'little bear', 'little truck', 'jeep', 'dump truck') — roles
- *Мама, папа, малыш* ('mom', 'dad', 'little one') — family

## Clarifications based on the IAA analysis

Double independent annotation of 30 books revealed several systematic disagreements between the annotators. The sections below are not new categories but clarifications of the existing rules, intended to reduce the number of contested cases in subsequent annotation rounds.

### Unique authorial name vs. descriptive role

The most frequent source of disagreement (116 of the 147 label-mismatch cases in the IAA analysis). Characters in children's books often receive a name derived from their role or an external attribute, and this does NOT make them PER_ROLE.

| **Feature** | **→ PER_NAME** | **→ PER_ROLE** |
| --- | --- | --- |
| Can you say "one of the [X]"? | No, this is a specific, one-of-a-kind character | Yes, it is a species designation / category |
| Does the word decline as a proper noun? | Yes (case forms exist: «Жёлтого», «к Жёлтому») | No, it is used as an ordinary noun |
| Is it used as a form of address to the character? | Yes | No |

- *«Обнимашка»* ('little hugger'; the protagonist little elephant) → PER_NAME — the only such character; declines («у Обнимашки»); used as a form of address.
- *«Жёлтый»* ('Yellow'; a character with a unique nickname) → PER_NAME — one cannot say "one of the yellows"; it declines.
- *«Одуванчики»* ('dandelions'; a group of flower characters) → PER_ROLE — a species designation for a group, not a unique nickname of a single character.

### Animal characters vs. animal species

Animals in children's literature are divided into specific acting characters and background mentions of a species.

| **Feature** | **→ PER_NAME (character)** | **→ PER_ROLE (species)** |
| --- | --- | --- |
| Unique name (may coincide with the species designation) | Yes, «Марабу» 'Marabou' as the teacher's name | No, simply «сова» 'owl', «снегирь» 'bullfinch' |
| Individual character traits, participation in dialogue | Yes | No |
| Used with a determiner/epithet («мудрая Сова» 'wise Owl') | Rarely | Often |
| Role in the plot | Significant, recurring | Episodic / background |

- *Марабу* 'Marabou' (a teacher with a name and dialogue lines) → PER_NAME.
- *мудрая Сова* 'wise Owl' (appears once, no dialogue, designated by species + epithet) → PER_ROLE.
- *Снегирь 'Bullfinch', Попугай 'Parrot'* (secondary characters without an individual name) → PER_ROLE

### A kinship role that has become a character's name

If a standard kinship word (*мама* 'mom', *папа* 'dad') is used by the author as part of a character's unique name (rather than as a mere mention of a relative), it is PER_NAME, not PER_FAMILY.

| **Example phrase** | **Label** | **Why** |
| --- | --- | --- |
| *Мама обняла его* ('Mom hugged him') | PER_FAMILY | Standard word denoting a kinship relation to the protagonist |
| *Обнимама* ('Hug-mom'; a character's name) | PER_NAME | A unique authorial word-name derived from the role "mom" |
| *Мама-Тигрица*, *Папа-Тигр* ('Mama-Tigress', 'Papa-Tiger') | PER_NAME | A compound authorial name; the kinship word is only its first part |

### Collective kinship terms: PER_ROLE vs. PER_FAMILY

*Дети* 'children', *родители* 'parents' without a clarifying possessive or an explicit link to a specific family are PER_ROLE, not PER_FAMILY.

| **Example phrase** | **Label** | **Why** |
| --- | --- | --- |
| *Дети бежали к морю* ('The children were running to the sea') | PER_ROLE | A generalized group; not the protagonist's specific siblings |
| *Его родители работали в саду* ('His parents worked in the garden') | PER_FAMILY | The possessive «его» 'his' explicitly anchors it to a specific character |
| *Мама обняла его* ('Mom hugged him') | PER_FAMILY | A specific kinship role relative to the protagonist |

### Span boundaries for compound names and designations

The most frequent technical source of annotation coordinate mismatches (boundary mismatch). Established from an analysis of actual disagreements: one annotator marks a compound name/designation as ONE span, the other as TWO separate spans, each with the same label.

| **Entity type** | **Example** | **Span rule** |
| --- | --- | --- |
| Two-word compound name | *Дед Мороз* 'Ded Moroz / Father Frost', *Керосин Бензинович* 'Kerosene Benzinovich' | ONE span over the entire name, label PER_NAME |
| Compound object/vehicle designation | *снегоуборочная машина* 'snow plow', *летняя уборочная машина* 'summer cleaning machine' | ONE span over the whole phrase, label PER_ROLE |

## What to do when in doubt

- If a case is not covered by any rule above, annotate by intuition and leave a short comment for later review.
- If in doubt between PER_NAME and PER_ROLE for a new, undescribed character type (plants, objects, natural phenomena) — apply the "can you say 'one of the [X]'?".

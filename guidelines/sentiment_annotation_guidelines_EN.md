# Sentiment Annotation Guidelines

*KidLit Project · Sentence-level sentiment annotation for 0+ literature · v2 (updated based on the IAA analysis)*

## General principles

You annotate the sentiment of every sentence in a children's book. The annotation unit is a single sentence. One of three labels is assigned.

### +1 — Positive

Assign +1 if the sentence evokes at least one of the following:

- joy, fun, laughter, play
- warmth, coziness, safety, relief
- hugs, reconciliation, reunion of loved ones
- praise, approval, pride, victory
- admiration of something beautiful or pleasant
- expression of love and care
- a happy ending, resolution of a conflict

### −1 — Negative

Assign −1 if the sentence creates a sense of:

- anxiety, fear, danger, darkness, threat
- sadness, loss, separation, loneliness
- anger, resentment, disappointment
- pain, tiredness, discomfort
- conflict, tantrums, disobedience (at the moment of tension)
- crying, panicked shouting, hysterics
- imaginary monsters or something frightening

### 0 — Neutral

Assign 0 if the sentence describes an action, movement, or fact without emotional load:

- description of place, time, or setting (without evident coziness or anxiety)
- neutral character actions: walks, looks, takes, rides
- questions without emotional load
- enumeration of events as narrative background
- dialogue framing phrases: said, answered, asked

## Difficult cases — decision rules

### Rule 1. The annotation unit is a single sentence

- *«Она не на шутку перепугалась.»* ('She got seriously frightened.') → −1
- *«Куда делся малыш?»* ('Where did the little one go?') → −1
- *«Но Тим притаился за кустом и молчит.»* ('But Tim hid behind a bush and keeps silent.') → −1

### Rule 2. Ambivalence — choose the dominant emotion

If a sentence contains both a positive and a negative component, assess which affects the child more strongly.

- *«— Я никогда не буду капризничать! — обещает Тим.»* ('"I will never throw tantrums again!" Tim promises.') → +1
  *(the promise and reconciliation outweigh the preceding conflict)*

### Rule 3. Exclamations — look at context, not the punctuation mark

- *«— Мамочка!»* ('Mommy!') → −1 (a cry in panic)
- *«— Вот ты где, Тим!»* ('There you are, Tim!') → +1 (relief at the reunion)
- *«— Хочу мороженое!»* ('I want ice cream!') → +1 (a joyful wish)
- *«— Не пойду!»* ('I won't go!') → −1 (protest)

＋ CLARIFICATION: exclamatory sentences with explicit markers of joy/delight (*«О!»*, *«Ура!»*, *«Как красиво!»* — 'Oh!', 'Hooray!', 'How beautiful!') are annotated as +1 POSITIVE automatically, even without additional context. If an exclamation contains no such marker and its emotional coloring is not evident from the sentence itself — assign 0 NEUTRAL rather than guessing from the general tone of the scene.

- *«О, это был самый настоящий цветущий сад!»* ('Oh, it was a real blossoming garden!') → +1 (the explicit delight marker «О»)

### Rule 4. Tantrums and conflict — label by the character's state

- *Tim throws a tantrum* → his distress → −1
- *Mom loses patience* → tension → −1
- *Tim promises to behave* → resolution → +1

### Rule 5. Scary things that get resolved

Assess the literal effect at the moment of reading:

- *«Мышонку кажется, что смотрят злые чудовища.»* ('The little mouse thinks evil monsters are watching.') → −1 (here it is fear, even if the monsters later turn out not to be real)
- *«И вдруг он понял, что никаких чудовищ нет.»* ('And suddenly he realized there were no monsters at all.') → +1 (relief, release)

＋ CLARIFICATION: if the mention of anxiety/fear and its resolution (care, support, comfort) occur WITHIN ONE sentence, the annotation follows the resulting emotion of the whole sentence, not the initial trigger word. The word «тревога» 'anxiety' or «страх» 'fear' inside a sentence does NOT automatically mean −1 if, by the meaning of the whole sentence, it is an act of care.

- *«— Мне бы хотелось спрятать тебя от всех тревог на свете.»* ('I would like to hide you from all the worries in the world.') → +1 (this is an expression of care that uses the word «тревоги» as part of a metaphor, not a description of the character's current fright)

⚠ Distinguish this from the opposite case: if a character realizes a mistake and expresses remorse, but the same or the following sentence contains NO immediate positive resolution — the label remains −1, even if the intonation is calm rather than panicked. *«— Значит, я зря обидел бегемотика… И обезьянку.»* ('So I hurt the little hippo for nothing… And the little monkey.') → −1 (remorse without resolution; not to be confused with the apology itself, which may form a separate +1 sentence).

### Rule 6. Physical states and nature

Descriptions of nature, weather, and physical sensations are annotated by their emotional effect in context, not by the dictionary meaning of the word itself. Warm sunshine against a sad scene does not make the sentence positive; a description of rain against a cozy domestic scene does not make the sentence negative.

### Rule 7. Dialogue framing phrases

- *«— говорит мама»* ('says mom') → 0 (a neutral speech verb)
- *«— кричит мама»* ('shouts mom') → −1 (if the shout stems from fear or anger)
- *«— смеётся мама»* ('laughs mom') → +1 (a positive verb)

The sentiment of the framing phrase is inherited from the emotion of the speech verb.

## Rule 8. Direct-speech utterance + speech verb — NEW RULE

Added following the IAA analysis: this was the most frequent source of segmentation mismatch between the annotators (over 500 cases out of ~3,360 matched sentence pairs).

＋ A direct-speech utterance and the IMMEDIATELY following speech verb with an intonational characteristic (*просил* 'begged', *выкрикнул* 'shouted out', *прошептал* 'whispered', *всхлипнул* 'sobbed') are annotated as ONE sentiment unit — one sentence for annotation purposes, even if they are visually separated by a dash or technically belong to different syntactic sentences.

- *«— Обними меня, мама! — просил он перед сном.»* ('"Hug me, mom!" he begged before bedtime.') → annotated as ONE sentence, labeled by the resulting emotion of the whole construction (+1: a request for closeness and warmth — not "hug me" separately plus a neutral "begged" separately).

Exception: if the speech verb itself carries independent emotional information distinct from the utterance and not derivable from it — separate annotation is permissible. This is an exception, not the default; in most cases the speech verb (*просил*, *сказал*, *ответил*, *прошептал*) only amplifies or neutrally introduces the tone of the utterance itself and does not contradict it.

⚠ If you are unsure which sentence the utterance belongs to syntactically — do not split artificially for the sake of formal punctuation compliance. Judge by meaning: the utterance + its immediate speech verb form a single semantic and emotional block.

## Quick reference

| **Category** | **Examples** | **Label** |
| --- | --- | --- |
| Explicit positive | joy, laughter, hugs, hooray | +1 POSITIVE |
| Explicit negative | fear, sadness, conflict, pain | −1 NEGATIVE |
| Neutral | facts, narration, neutral dialogue | 0 NEUTRAL |
| Exclamation with an explicit joy marker | «О!», «Ура!», «Как красиво!» | +1 POSITIVE |
| Anxiety-as-metaphor with care in the same sentence | «спрятать тебя от тревог» | By the resulting emotion (often +1) |
| Remorse without resolution in the same/following sentence | «я зря обидел…» | −1 NEGATIVE |
| Utterance + speech verb | «— Обними меня! — просил он» | ONE sentence, labeled by the resulting emotion |
| Mixed | context analysis | Choose the dominant emotion |

## Label Studio XML configuration (shared with NER)

```xml
<View>
  <Header value="$title" style="font-size: 16px; font-weight: bold; color: #555;"/>
  <Labels name="label" toName="text">
    <!-- NER — unchanged -->
    <Label value="PER_NAME"   background="#2980B9" hotkey="1"/>
    <Label value="PER_ROLE"   background="#E67E22" hotkey="2"/>
    <Label value="PER_FAMILY" background="#8E44AD" hotkey="3"/>
    <!-- Sentiment — new labels -->
    <Label value="+1 POSITIVE"   background="#1e8449" hotkey="4"/>
    <Label value="0 NEUTRAL" background="#616a6b" hotkey="5"/>
    <Label value="-1 NEGATIVE"   background="#c0392b" hotkey="6"/>
  </Labels>
  <Text name="text" value="$text" granularity="word"/>
  <!-- Hint -->
  <View style="margin-top:10px; padding:8px 14px; background:#fef9e7;
               border-left:4px solid #f39c12; border-radius:4px;">
    <Header value="NER: 1 = PER_NAME · 2 = PER_ROLE · 3 = PER_FAMILY   |   Sentiment: 4 = +1 POSITIVE · 5 = 0 NEUTRAL · 6 = -1 NEGATIVE"
            style="font-size:11px; color:#7f8c8d;"/>
  </View>
</View>
```

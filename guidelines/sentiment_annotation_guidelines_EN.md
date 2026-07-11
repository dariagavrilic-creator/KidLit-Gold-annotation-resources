# Sentiment Annotation Guidelines

*KidLit Project*

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

**The main rule:** evaluate the **emotional effect** of a sentence on a child reader (listener in this case), not the formal meaning of the words. Children's literature works through **imagery and intonation**, not through direct "good/bad" language.

## Difficult cases — decision rules

### –	#1 Sentence Independence Rule. 
**The annotation unit is a single sentence; the label is assigned independently of neighboring sentences.**

- *«Она не на шутку перепугалась.»* ('She got seriously frightened.') → −1
- *«Куда делся малыш?»* ('Where did the little one go?') → −1
- *«Но Тим притаился за кустом и молчит.»* ('But Tim hid behind a bush and keeps silent.') → −1

### –	#2 Dominant Emotion Rule. 
**If a sentence contains both a positive and a negative component, the annotator assesses which of them affects the child more strongly.**

- *«— Я никогда не буду капризничать! — обещает Тим.»* ('"I will never throw tantrums again!" Tim promises.') → +1
  *(the promise and reconciliation outweigh the preceding conflict)*

### –	#3 Contextual Exclamation Rule
**Polarity is determined by context rather than punctuation.**

- *«— Мамочка!»* ('Mommy!') → −1 (a cry in panic)
- *«— Вот ты где, Тим!»* ('There you are, Tim!') → +1 (relief at the reunion)
- *«— Хочу мороженое!»* ('I want ice cream!') → +1 (a joyful wish)
- *«— Не пойду!»* ('I won't go!') → −1 (protest)
- *«О, это был самый настоящий цветущий сад!»* ('Oh, it was a real blossoming garden!') → +1 (the explicit delight marker *О* 'Oh')

### –	#4 Emotional State Rule
**Tantrums and conflict are labeled according to the character's emotional state at the moment of action, not according to a moral evaluation of the behavior.**

- *Tim throws a tantrum* → his distress → −1
- *Mom loses patience* → tension → −1
- *Tim promises to behave* → resolution → +1

### –	#5 Immediate Effect Rule. 
**Sentiment is judged by the reader's emotional response at the moment of reading, not by the eventual resolution of the situation.**

- *«Мышонку кажется, что смотрят злые чудовища.»* ('The little mouse thinks evil monsters are watching.') → −1 (here it is fear, even if the monsters later turn out not to be real)
- *«И вдруг он понял, что никаких чудовищ нет.»* ('And suddenly he realized there were no monsters at all.') → +1 (relief, release)
- *«— Мне бы хотелось спрятать тебя от всех тревог на свете.»* ('I would like to hide you from all the worries in the world.') → +1 (this is an expression of care that uses the word *тревоги* 'worries' as part of a metaphor, not a description of the character's current fright)

⚠ Distinguish this from the opposite case: if a character realizes a mistake and expresses remorse, but the same or the following sentence contains NO immediate positive resolution — the label remains −1, even if the intonation is calm rather than panicked. *«— Значит, я зря обидел бегемотика… И обезьянку.»* ('So I hurt the little hippo for nothing… And the little monkey.') → −1 (remorse without resolution; not to be confused with the apology itself, which may form a separate +1 sentence).

### –	#6 Emotional Effect Rule
**Physical states and descriptions of nature are assessed by their emotional effect, not by the factual neutrality of the phenomenon described.**

Descriptions of nature, weather, and physical sensations are annotated by their emotional effect in context, not by the dictionary meaning of the word itself. Warm sunshine against a sad scene does not make the sentence positive; a description of rain against a cozy domestic scene does not make the sentence negative.

### –	#7 Inheritance of Sentiment Rule
**Dialogue framing phrases inherit the sentiment of the speech verb.**

- *«— говорит мама»* ('says mom') → 0 (a neutral speech verb)
- *«— кричит мама»* ('shouts mom') → −1 (if the shout stems from fear or anger)
- *«— смеётся мама»* ('laughs mom') → +1 (a positive verb)

The sentiment of the framing phrase is inherited from the emotion of the speech verb.

## #8 Intonational Link Rule
**A direct-speech utterance and the immediately following speech verb with an intonational characteristic are annotated as a single sentiment unit if the speech verb carries no emotional information distinct from that of the utterance itself.**

＋ A direct-speech utterance and the IMMEDIATELY following speech verb with an intonational characteristic (*просил* 'begged', *выкрикнул* 'shouted out', *прошептал* 'whispered', *всхлипнул* 'sobbed') are annotated as ONE sentiment unit — one sentence for annotation purposes, even if they are visually separated by a dash or technically belong to different syntactic sentences.

- *«— Обними меня, мама! — просил он перед сном.»* ('"Hug me, mom!" he begged before bedtime.') → annotated as ONE sentence, labeled by the resulting emotion of the whole construction (+1: a request for closeness and warmth — not "hug me" separately plus a neutral "begged" separately).

⚠ If you are unsure which sentence the utterance belongs to syntactically, do not split artificially for the sake of formal punctuation compliance. Judge by meaning: the utterance + its immediate speech verb form a single semantic and emotional block.

## Quick reference

| **Category** | **Examples** | **Label** |
| --- | --- | --- |
| Explicit positive | joy, laughter, hugs, hooray | +1 POSITIVE |
| Explicit negative | fear, sadness, conflict, pain | −1 NEGATIVE |
| Neutral | facts, narration, neutral dialogue | 0 NEUTRAL |
| Exclamation with an explicit joy marker | «О!» 'Oh!', «Ура!» 'Hooray!', «Как красиво!» 'What a beauty!' | +1 POSITIVE |
| Anxiety-as-metaphor with care in the same sentence | «спрятать тебя от тревог» 'to hide you from all the worries' | By the resulting emotion (often +1) |
| Remorse without resolution in the same/following sentence | «я зря обидел…» 'hurt for nothing' | −1 NEGATIVE |
| Utterance + speech verb | «— Обними меня! — просил он» '"Hug me!" he begged' | ONE sentence, labeled by the resulting emotion |
| Mixed | context analysis | Choose the dominant emotion |

## Useful Tip 
**If you're unsure between two markers, ask yourself:**
*If I were reading this aloud to a child, how would I change the intonation?*   
<span style="color:red;">Anxious intonation</span> → -1 <span style="color:green;">Joyful intonation</span> → +1 <span style="color:grey;">Even intonation</span> → 0


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

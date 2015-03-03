This is where the RCC will share project related work for the [Thirty-Million-Word
Initiative](http://tmw.org/).

---

The TMW Initiative is seeking immediate assistance with the construction of a
database of speech utterances based on newly transribed speech samples
(mother/child interactions) of the various participants in their longitudinal
study.  In addition to converting and validating the provided transcripts (as preliminary steps for generating the utterance dataset), they are requesting a basic speech analysis of the utterance dataset (viz., they would like the following speech measures/counts for each speaker (parent and child) at each available time point:

* MLU (mean length of utterance)
* count of utterance fields containing at least one letter
* word token count (# of word tokens, using default tokenization)
* word type count (# of **unique** word tokens, unlemmatized)

This analysis will utilize [the LDP's existing python API](https://github.com/joyrexus/ldp/blob/master/code/lib/python/ldp/speech.py) and [transcript staging utilities](https://github.com/joyrexus/ldp/tree/master/code/stage).

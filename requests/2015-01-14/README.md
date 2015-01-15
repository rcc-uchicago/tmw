# 2015-01-14 

The TMW Initiative is seeking immediate assistance with the construction of a
database of speech utterances based on newly transribed speech samples
of the subjects in their longitudinal language study.  In addition to converting and validating the provided transcripts (as preliminary steps for generating the utterance dataset), they would like a summary analysis of the utterance dataset.

In particular, they would like a summary report consisting of the following speech measures/counts for each speaker (parent and child) at each available time point:

* MLU (mean length of utterance)
* count of utterance fields containing at least one letter
* word token count (# of word tokens, using default tokenization)
* word type count (# of **unique** word tokens, unlemmatized)

This analysis would utilize [the LDP's existing python
API](https://github.com/joyrexus/ldp/blob/master/code/lib/python/ldp/speech.py) and utilities, which should only require moderate customization for their dataset (i.e., the utterance dataset we'd be generating based on the new TMW transcript collection).

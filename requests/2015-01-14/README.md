# 2015-01-14 

The TMW Initiative is seeking immediate assistance with the construction of a
database of speech utterances based on newly transribed speech samples
(mother/child interactions) of the various participants in their longitudinal
study.  In addition to converting and validating the provided transcripts (as preliminary steps for generating the utterance dataset), they are requesting a basic speech analysis of the utterance dataset (viz., they would like the following speech measures/counts for each speaker (parent and child) at each available time point:

* MLU (mean length of utterance)
* count of utterance fields containing at least one letter
* word token count (# of word tokens, using default tokenization)
* word type count (# of **unique** word tokens, unlemmatized)

This analysis would utilize [the LDP's existing python API](https://github.com/joyrexus/ldp/blob/master/code/lib/python/ldp/speech.py) and [transcript staging utilities](https://github.com/joyrexus/ldp/tree/master/code/stage). Both the API and staging utilities should only require moderate customization for their dataset (i.e., the utterance dataset we'd be generating based on the new TMW transcript collection).

In addition to addressing the immediate need for a summary report of speech
measures/counts, we'll assist the TMW initiative with the preservation, reuse, and extension of the TMW's core research dataset (a unified database of queryable speech utterances) in a manner analogous to the Language Development Project's longitudinal dataset. This will enable it be used for follow-up analyses, replicating existing analyses, or shared with disciplinary research archive, such as [Databrary](https://databrary.org/), if the TMW wishes to share their work with the community of developmental researchers.

# 2015-03-03

Eileen Graf provided a set of transcripts from the Thirty Million Words
project.  She'd like speech counts (mlu, utterances, word tokens, word 
types) for each speaker (parent and child) at each time point (PRE, POST1, 
POST2).


## Report Columns

* `subj` - subject ID
* `sess` - session ID (`1` = PRE, `2` = POST1, `3` = POST2)
* `spkr` - speaker (`P` = parent, `C` = child)
* `UTT` - count of utterance fields containing at least one letter
* `TOK` - word token count
* `TYP` - word type count (i.e., # of unique word tokens, unlemmatized)
* `MLU` - mean length of utterance


## Notes

> In the previously provided dataset, each participant had 3 data points: `PRE`, `POST1`, `POST2`). For the new dataset ...

> each participant¹s full transcript was split into 2 transcripts, because each session comprised a book reading part (A) and a free play (B) part which, theoretically, shouldn¹t be lumped together.  

So, there are 6 data points per subject (or fewer, since not all participants completed all three sessions, and not everybody read a book) - there are 3 sessions and each session splits into [a,b].


## Session mapping

* `1` - `pre-A` 
* `2` - `pre-B`
* `3` - `post-1-A`
* `4` - `post-1-B`
* `5` - `post-2-A`
* `6` - `post-2-B`

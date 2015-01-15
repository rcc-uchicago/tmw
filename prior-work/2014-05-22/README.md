# 2014-05-22 

Eileen Graf provided a set of transcripts from the Thirty Million Words
project.  She'd like speech counts (mlu, utterances, word tokens, word 
types) for each speaker (parent and child) at each time point (PRE, POST1, 
POST2).

See the resulting [report](report.revised.xls).


## Report Columns

* `subj` - subject ID
* `sess` - session ID (`1` = PRE, `2` = POST1, `3` = POST2)
* `spkr` - speaker (`P` = parent, `C` = child)
* `UTT` - count of utterance fields containing at least one letter
* `TOK` - word token count
* `TYP` - word type count (i.e., # of unique word tokens, unlemmatized)
* `MLU` - mean length of utterance


#### Request (May 22, 2014)
  
> There are 3 subfolders according to time point (each participant has 3 
> data points: `PRE`, `POST1`, `POST2`). We’d need the numbers (MLU, utterance, 
> type, token) for each participant (parent and child separately) at each 
> time point. 

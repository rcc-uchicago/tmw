# 2015-03-03

Eileen Graf provided an additional set of transcripts from the Thirty Million Words project for processing and analysis (identical to what was done for the [prior request](https://github.com/rcc-uchicago/tmw/tree/master/requests/2015-03-03#2015-03-03)).

She'd like speech counts (mlu, utterances, word tokens, word types) for each speaker (parent and child) at each time point (**PRE-A**, **PRE-B**, **POST-1-B**, etc.). See below for notes on time points / sessions and how they're coded in the summary speech report.

The resulting summary speech report can be found [here](report.tsv).


## Session mapping

* `1` - **PRE-A**
* `2` - **PRE-B**
* `3` - **POST-1-A**
* `4` - **POST-1-B**
* `5` - **POST-2-A**
* `6` - **POST-2-B**


## Report Columns

* `subj` - subject ID
* `sess` - session ID (`1` = **PRE-A**, `2` = **PRE-B**, `3` = **POST-1-A**, ...)
* `spkr` - speaker (`P` = parent, `C` = child)
* `UTT` - count of utterance fields containing at least one letter
* `TOK` - word token count
* `TYP` - word type count (i.e., # of unique word tokens, unlemmatized)
* `MLU` - mean length of utterance


## Notes

In the previously provided dataset, each participant had 3 data points: `PRE`, `POST1`, `POST2`). For the new dataset ...

> each participant¹s full transcript was split into 2 transcripts, because each session comprised a book reading part (A) and a free play (B) part which, theoretically, shouldn¹t be lumped together.  

So, there are 6 data points per subject (or fewer, since not all participants completed all three sessions, and not everybody read a book): 3 visits (**PRE**, **POST-1**, **POST-2**) and each visit is of two types (**A** and **B**).

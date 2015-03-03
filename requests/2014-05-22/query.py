from ldp.speech import Report

speech = Report(lemmatize=False, dataset='data/data.db')
speech.query()
speech.report()

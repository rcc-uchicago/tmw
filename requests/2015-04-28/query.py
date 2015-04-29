from ldp.speech import Report

speech = Report(lemmatize=True, dataset='data/data.db')
speech.query()
speech.report()

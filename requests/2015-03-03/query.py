from ldp.speech import Report

speech = Report(lemmatize=True, dataset='data.db')
speech.query()
speech.report()

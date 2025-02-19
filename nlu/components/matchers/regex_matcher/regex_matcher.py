import sparknlp

class RegexMatcher:
    @staticmethod
    def get_default_model():
        return sparknlp.annotator.RegexMatcher()\
            .setInputCols("sentence") \
            .setOutputCol("regex_entity") \
            

    @staticmethod
    def get_pretrained_model(name, language, bucket=None):
        return RegexMatcher.get_default_model()
        # sparknlp.annotator.TextMatcherModel.pretrained(name,language,bucket) \
        #     .setInputCols("document") \
        #     .setOutputCol("entity") \



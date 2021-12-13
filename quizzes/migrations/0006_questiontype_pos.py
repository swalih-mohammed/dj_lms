# Generated by Django 3.2.7 on 2021-12-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_auto_20211213_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='questiontype',
            name='pos',
            field=models.CharField(choices=[('NotPos', 'NotPos'), ('Noun', 'Noun'), ('Singular', 'Singular'), ('Place', 'Place'), ('ProperNoun', 'ProperNoun'), ('Plural', 'Plural'), ('Uncountable', 'Uncountable'), ('Possessive', 'Possessive'), ('Verb', 'Verb'), ('PresentTense', 'PresentTense'), ('Infinitive', 'Infinitive'), ('Gerund', 'Gerund'), ('PastTense', 'PastTense'), ('PerfectTense', 'PerfectTense'), ('FuturePerfect', 'FuturePerfect'), ('Participle', 'Participle'), ('PhrasalVerb', 'PhrasalVerb'), ('Adjective', 'Adjective'), ('Negative', 'Negative'), ('Superlative', 'Superlative'), ('Comparative', 'Comparative'), ('Adverb', 'Adverb'), ('Preposition', 'Preposition'), ('QuestionWord', 'QuestionWord'), ('Pronoun', 'Pronoun')], default='NotPos', max_length=250),
        ),
    ]

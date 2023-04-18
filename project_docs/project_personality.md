## Project option 1

### Overview

This project is designed basically to take what you've already done in homework assignments and adapt that to a new problem.  The basic process here is surprisingly applicable in the real world -- many, many problems you encounter involve text classification, and it's often better to start with something straightforward and understandable like logistic regression rather than jumping into bleeding-edge deep learning approaches.

Here in Project option 1, what you'll be doing is based on the [2013 Workshop on Computational Personality Recognition Shared Task](https://www.semanticscholar.org/paper/Workshop-on-Computational-Personality-Recognition%3A-Celli-Pianesi/92a7d4c5d7ba16e8434aeeaaa406237dd5c8b22b). (See [Project option 2](project_sw.md) for basically the same work, but on a different dataset you also might find interesting.) It's recommended that you read the overview paper (it's only four pages) for fuller context, but the basic idea here is that you have written data from a sample of individuals, and for each individual you also have information about their personality as measured by the Big-5 Personality Inventory, a validated and widely used way of measuring individuals' personality traits. (Note: Meyers-Briggs shows up a lot in the popular press for characterizing personality, but I have it on good authority that it is trash.)  

In addition to providing a useful sandbox for exploring NLP and machine learning techniques, personality traits are of significant real-world interest because they connect with people's lived experiences in important ways.  For example, the personality trait known as neuroticism tends to be correlated with depression, and the trait of conscientiousness is one of the strongest predictors of success in the workplace.  In addition, the data for this project are very reasonable in size, which means you should have no difficulty doing the work on a laptop if you don't have access to more powerful computing resources.

*Groups are encouraged to be generous toward other groups; this is not a competition.  If you figure something out that might save other people trouble, please share it on Slack or with the Insructor.  If you are the beneficiary of someone else sharing information, e.g. it helped you save some time, avoid an error, understand something better, etc., please say so in your writeup. I will make sure that such generosity is taken into account in grading.*

### Data

There are two (fully de-identified) datasets, `myPersonality` and `Essays`. You are going to develop a model to predict neuroticism (the cNEU variable) using the myPersonality data. An optional extension will be to use your trained model to see how well you can predict neuroticism for individuals in the `Essays` dataset.

- **myPersonality.**  Status updates from individuals on social media, along with numeric and nominal (numbers converted to yes/no) measures of their Big-5 personality traits (OCEAN: openness, conscientiousness, extraversion, agreeableness, and neuroticism), along with some other metadata that we won't be using. For example, here are two status updates from a user:

```
"#AUTHID","STATUS","sEXT","sNEU","sAGR","sCON","sOPN","cEXT","cNEU","cAGR","cCON","cOPN","DATE","NETWORKSIZE","BETWEENNESS","NBETWEENNESS","DENSITY","BROKERAGE","NBROKERAGE","TRANSITIVITY"
"b7b7764cfa1c523e4e93ab2a79a946c4","Why is it I'm only getting the urge to draw when I have stuff to do for school? D;",2.65,3.00,3.15,3.25,4.40,"n","y","n","n","y",08/26/09 12:16 AM,180,14861.6,93.29,0.03,15661,0.49,0.1
"b7b7764cfa1c523e4e93ab2a79a946c4","wishes to develop a super power that prevents her from needing to sleep.",2.65,3.00,3.15,3.25,4.40,"n","y","n","n","y",09/01/09 02:05 AM,180,14861.6,93.29,0.03,15661,0.49,0.1
```

- **Essays.**  A set of stream-of-consciousness texts written by college students, accompanied by nominal (yes/no) Big-5 personality labels.

```
"#AUTHID","TEXT","cEXT","cNEU","cAGR","cCON","cOPN"
"1997_504851.txt","Well, right now I just woke up from a mid-day nap. It's sort of weird, but ever since I moved to Texas, I have had problems concentrating on things. I remember starting my homework in  10th grade as soon as the clock struck 4 and not stopping until it was done. ... ","n","y","y","n","y"
```

### Steps and how to write things up

Your writeup should start at the top by identifying the members of your group and who contributed to what steps below.  The more you work together the better, though I know logistics can be tough these days. I encourage you to have at least two people on each step if possible rather than divide-and-conquer, and you *definitely* should take the effort to provide an integrated writeup that everyone has contributed to.

Each of these steps should get a section in your writeup that clearly describes what you did, why, and what you found.  Note that you do *not* need to spit back textbook definitions, e.g. it's sufficient to say "We built a logistic regression model" without providing the equations for logistic regression. That said, aim for a writeup that demonstrates thought, insight, and understanding.  Note that there really are no "correct" outcomes here, *per se* -- this is an open ended problem.  You are welcome to use any code I have provided, and of course any code you have already written.  You are even welcome to use code you find on the web, as long as you properly cite your sources; adapting other people's code for your purposes is a really important skill.

- **Initial data analysis.**  Get a feel for the problem, using training data in the [myPersonality](data/README.md) dataset after wranging the original data into a convenient form (e.g. [producing jsonlines from the CSV file](https://stackoverflow.com/questions/19697846/how-to-convert-csv-file-to-multiline-json) so it's easy to adapt your previously-written code), then doing a train/test split.  One obvious way to do this would be to look at unigrams and bigrams, seeing which are more associated with one or the other label in the training data (e.g. using [log-likelihood ratio](https://github.com/tdunning/python-llr) or PMI). You could also consider questions like, does it make sense to include punctuation tokens, or exclude them?  Do you see any reason to use lemmas versus the fully inflected form of the word? Does the tokenizer you're planning to use (e.g. spaCy's by default as in the assignments) do a good job on this kind of data?  Do you see any patterns evident that might inform your thinking on how to distinguish individuals with a *yes* versus *no* label for neuroticism?  

	In your writeup talk about what you did, including your motivations and what you found (similar in spirit to the writeup in Assignment 1).

- **Baseline classifier.**  Build a baseline binary classifier to label individual users with *yes* or *no* for neuroticism using the `myPersonality` dataset. For this baseline a default option would be to adapt the logistic regression approach we took in Assignment 2, using unigrams and bigrams as features -- you already have all the building blocks and the baseline is merely a matter of wrangling the data into the right format. It would be great to do k-fold cross validation (I recommend stratified if there's significant label imbalance), but a single train-test split is also ok.

	If you prefer to explore state of the art methods at any point (baseline or later), you are welcome to. The current standard would be to use a pretrained transformer (e.g., BERT) model and then fine-tune it for the specific task.  You can find many tutorials/examples on how to do this by searching on *bert for sequence classification fine-tuning tutorial* -- on a quick look, [this one](https://www.thepythoncode.com/article/finetuning-bert-using-huggingface-transformers-python) looks well explained and straightforward. If you go that route, my recommendation would be to start with the tutorial, make sure you can run it successfully end to end, and then mirror it step-by-step while adapting it to this specific classification problem.  Note, though, that you should not put this on the [critical path](https://2020projectmanagement.com/resources/project-planning/what-is-the-critical-path) for your project unless you are confident that you can do it; it's better to do solid, thoughtful work and produce a good writeup than to push the boundaries and not succeed in getting all the way through the project.

	***Important note.*** regardless of your classification approach, note that, because the task is to label *users*, not *posts*, you won't simply be treating each post as a labeled item. Instead, you have several choices for doing labeling at the user level.

	- Simplest would be to collect all of an individual's posts into a single long document, giving that aggregated document the user's label (which should be the same for all their posts). It would be easy to turn the post-level input file into a user-level input file by doing that, and then everything is pretty much the same as Assignment 2 with the user's aggregated document as the document to be classified.
	- You could treat each post (or, for example, posts within some given time interval) as a separate item for classification, build a classifier, and then aggregate the item labels into a single label prediction for the user. As one possibility, if more than X% of a user's items are classified as *yes*, then classify the user as a yes. (An obvious choice would be 50%, but you could vary X as a tunable parameter and see what works best.) This adds some additional complexity in terms of code you'd need to write.

	Whatever decision you make for making this amenable for user labelling, make sure that the expected input for your NLP pipeline is treated in the same way for all splits of your data (training, validation, test, etc.).

- **Improving classification.**  See if you can improve performance using the `myPersonality` data, doing formative evaluations along the way.  Some things to consider trying:
	- Adding lexical features.  Consider using the Linguistic Inquiry and Word Count ([LIWC](resources/README.md)) lexicon and augment your document representation with selected category features. For example, suppose you decided that relevant LIWC categories included categories 4 (first-person singular pronoun), 126 (posemo, i.e. positive emotion), and 127 (negemo, i.e. negative emotion).  If the document is *i love dogs* you might add nominal features {*liwc_i*, *liwc_posemo*} based on the fact that the sentence includes the words *I* and *love* respectively. (Note that in LIWC, some words are specified as stems, e.g. *worr\** as a prefix that would match {*worry*, *worried*, *worries*, *worrying*}. Alternatively, you might consider using [Empath](https://github.com/Ejhfast/empath-client) categories the same way.  Either way, an interesting choice would be whether to add these as a binary feature (e.g. *negemo* is present once, as long as at least one word is in that category) or as a count feature (e.g. adding a *negemo* unigram for every token that's in that category).
	- Adding syntactically based features.  Would it make more sense to use noun phrases (e.g. identified using spaCy's NP chunker) instead of or in addition to bigram features? (Note: in my experience it's good to strip leading stopwords from noun phrases, e.g. [NP *some of the cool professors*] becomes *cool_professors*.) Might there be particular syntactic combinations that could be a useful indicator for neuroticism, maybe in combination with lexical categories like anxiety or negative emotion?  For example, would *negemo verb with first-person subject* (e.g. "I hate") be something that might be more valuable than just features of the words independently?
	- Feature selection.  Rather than considering all possible features, instead select those that are more strongly associated statistically with one label or the other, e.g. measuring that using log-likelihood ratio or PMI.  
	- Using a different classifier.  E.g. instead of logistic regression, use SVM and/or random forest classification.  Or forget about traditional machine learning classifiers and feature extraction, and instead switch to a state of the art sequence classifier approach (see above).
	- Parameter tuning.  Try different combinations of parameters of your model (e.g. via grid search), evaluating each combination using cross-validation; freeze the best set of parameters; run that classifier on the test data.
	- Do error analysis, looking at misses and/or false positives to see what kinds of mistakes are made by your classifier(s).  This might guide some of the above choices, i.e. doing error analysis in a formative way, and/or you could include a summative error analysis on the test data as another section.

	These ways of trying to improve classification are not mutually exclusive, and they are *definitely* not exhaustive. If you have ideas for other things you're thinking of trying, I recommend running them by me (sooner the better) -- I might be able to provide a reality check, e.g. if I believe something is going to be more work than you think it is.

	In this section, make sure you have clearly stated experimental details like how you divided up your data, proportions for train/test split, number of folds for cross-validation, whether or not you stratified if you need cross-validation, etc.

	Note that you do *not* need to succeed in improving over the baseline, though of course that's a very satisfying feeling when you can manage it.


The above steps are expected, and should be feasible for a typical group to do, end-to-end and satisfactorily, in the allotted time.  If you'd like to take this one more step toward the real world:

- **Evaluating on a new dataset.**	Run (a) your baseline, and (b) at least one attempt at an improved classifier, on the [Essays](data/README.md) data, predicting the neuroticism label for individuals.

	Note that this is a step beyond what you've done in the assignments.  Up to this point you've taken a single dataset `(X,y)`, broken it into `(X_train,y_train,X_test,y_test)` and/or run cross-validation. Now in addition to that, you need to read a *new* dataset, preprocess it and do feature extraction the same way (e.g. using the same vectorizer for the first dataset), and use your trained model to make predictions, and then evaluate.

- **Submission** Again, we expect a comprehensive writeup in a `writeup.pdf` detailing what you did and how you conducted your evaluation, along with the code used, and specific instructions on how to run it to build and train your model, etc. This is so that if need be, we could *reproduce* your experiments and get the same results. So please make this as nice and clean as possible, and to keep this in mind at the very beginning, so that iteration can be easier on your part as well!

**Have fun!**

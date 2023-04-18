## Project option 2

### Overview

*Please start by reading through [Project option 1](project_personality.md). What you have here is basically the same project, with the same requirements, but doing the work on a different dataset/classification problem that you might find compelling or interesting. Therefore you should consider the instructions there to be the overview for this project also.  Let us know if you find antyhing confusing or unclear.*

### Caution

If you choose to do this project, you will be looking at posts written by users in an online discussion forum. The dataset comes from an ongoing research project where the goal is finding new ways to help prevent suicides.

Before you go any further, please recognize that some of the posts you might see were written by people in real distress, and they can be difficult or upsetting to read. If you think that you might be affected personally in a negative way by doing this project, please err on the side of caution and stop here; do not do the project — an alternative project is available. If you start the project and you find that it’s upsetting, similarly, please stop and contact the instructor to make an alternative project plan.

If you’re feeling like you (or someone you know) could use some support or assistance, please take advantage of one of the following resources:

- National Suicide Prevention Lifeline: 1-800-273-8255 (TALK). – Veterans please press 1 to reach specialized support.
- Spanish: 1-800-SUICIDA
- Crisis Text Line: Text ”START” to 741-741
- Online chat: http://www.suicidepreventionlifeline.org/gethelp/lifelinechat.aspx
- https://www.reddit.com/r/SuicideWatch/wiki/hotlines - This page provides information about phone and chat hotlines and online resources in the U.S. and worldwide.

Please note that all the posts you will encounter in this project were anonymous — not even the researchers who created the dataset know who these people are, and the posts were made over a period of years. Although it’s tragic that there is no direct way for us to help the people who have written these posts who may be at risk of suicide, work on this dataset is aimed at better understanding the factors connected with suicide attempts, using that information to do a better job assessing risk, and hopefully contributing to more effective ways of getting people help.

Also, although the posts we’re working with are anonymous, and even though the aim in this project is pedagogical, not research, it is important that you read and understand the section below on ethical use of social media data.

### Dataset

The data you will work with in this project come from the [UMD Reddit Suicidality Dataset](https://umiacs.umd.edu/~resnik/umd_reddit_suicidality_dataset.html).  The dataset is described in [Shing et al. (2018)](http://aclweb.org/anthology/W18-0603).  Because the data are considered sensitive, your group will need to follow the steps below under "Requesting the Dataset" in order to get the data to work with.

[Reddit](http://en.wikipedia.org/wiki/Anonymous_social_media) is an anonymous social media site in which anonymous users submit posts to areas of interest called ‘subreddits’. Shing et al. (2018) provides a detailed description of how the dataset was constructed from a large collection of every publicly available Reddit posting from January 1, 2008 through August 31, 2015 (with partial data from 2006-2007). Briefly:

- We identified the 11,129 users who had ever posted to r/SuicideWatch (which we’ll sometimes abbreviate as SW), a discussion forum where the aim is to provide peer support for people considering suicide. Posters on SW generally tend to fall into one of three categories’: people who themselves are considering the possibility of self-harm, people who are worried about a friend or loved one, and people who want to help. The fact that someone posted to SuicideWatch can be viewed as a form of indirect supervision, i.e. a noisy indicator of possible suicidality.

- Of those 11,129 users, a subset of 934 were randomly selected, and crowdsource workers labeled each individual on a four-point scale for risk based on reading their SW postings. Those risk labels can be viewed as a moderately reliable labeling for risk, based on our analysis of inter-rater agreement.

- Of those 934 users, a subset of 242 were labeled on the four-point risk scale by four experts in suicide prevention looking at their SW posts. Each individual was looked at by all four experts, and the inter-expert reliability (agreement on risk levels) was high, so their consensus ratings can reasonably be considered ground truth. The four labels are:

	(a) No Risk (or “None”): I don’t see evidence that this person is at risk for suicide;

	(b) Low Risk: There may be some factors here that could suggest risk, but I don’t really think this person is at much of a risk of suicide;

	(c) Moderate Risk: I see indications that there could be a genuine risk of this person making a suicide attempt;

	(d) Severe Risk: I believe this person is at high risk of attempting suicide in the near future.

Shing et al. (2018) provide detailed discussion of the rubrics for annotation, etc.


### Task

- The task here is binary classification where label (d), Severe Risk, constitutes the positive label, and labels (a)-(c) are mapped to the negative label. This corresponds directly to the binary yes/no labeling in Project option 1.  It also corresponds to Task A in the CLPsych 2019 Shared Task, [Zirikly et al (2019)](https://scholar.google.com/scholar_url?url=https://www.aclweb.org/anthology/W19-3003.pdf&hl=en&sa=T&oi=gsb-gga&ct=res&cd=0&d=8391027893644468791&ei=4k9_YOvLNJD_mAGorriYDA&scisig=AAGBfm1xR0U5vh1goWbuWIBgeHQWViCcgA).

- The crowdsource-labeled data corresponds directly to use of the `myPersonality` data in Project option 1.  It is the dataset you'll use for the main project steps under "Steps and how to write things up" in Project option 1.

- The expert-annotated data corresponds directly to the use of the `Essays` data in Project option 1.  It is the dataset you can use if so desired for "Evaluating on a new dataset" as discussed in Project option 1.


	*As noted in Project option 1, groups are encouraged to be generous toward other groups; this is not a competition.  If you figure something out that might save other people trouble, please share it on Piazza.  If you are the beneficiary of someone else sharing information, e.g. it helped you save some time, avoid an error, understand something better, etc., please say so in your writeup. I will make sure that such generosity is taken into account in grading.*

### Ethical use of social media data

Whenever you’re working with data that originates with human beings, it’s important to spend some time thinking about appropriate uses of the data both in terms of official rules, and in terms of broader ethical considerations whether or not those are officially mandated.

As an important starting point, “human subjects research” is defined as (a) a systematic investigation, including research development, testing, and evaluation, designed to develop or contribute to generalizable knowledge, that involves (b) a living individual about whom a research investigator obtains data through intervention or interaction with the individual, or individually identifiable information. In the U.S., the official definition of human subjects research and the rules surrounding it grew out of abuses that took place in the absence of formalized regulation when researchers convinced themselves that the benefits of their studies outweighed what should have been obvious harms. At universities (and many other organizations), the proper conduct of human subjects research are overseen by a committee called an Institutional Review Board, or IRB.

Formally speaking, this project is actually not human subjects research, for two reasons. First, in general class assignments are not research, because they are intended to help train students or give them experience with research methods, as opposed to collecting information systematically with the intent to develop or contribute to generalizable knowledge. (The intent matters: I hope you’ll learn enough from this assignment to be able to do good research, possibly even to follow up this class assignment with a real research project,  but the work you’re doing for this project during this semester is not intended to produce publications.) In addition, this project in particular doesn’t involve human subjects research according to the formal definition: we are working with publicly available social media behavior, which involves neither intervention, nor interaction with individuals, nor individually identifiable information, since Reddit is an anonymous social media site and the data have gone through another layer of automatic de-identification as an additional safeguard.

That said, any project involving social media needs to be handled with great sensitivity, particularly when touchy issues like mental health are involved. It is important, therefore, that you not disseminate or share the data we are working with, and it would also be completely inappropriate to use Web searches to look for further information from or about a user in these datasets, even for benign purposes. Following [Benton et al. (2017)](https://www.aclweb.org/anthology/W17-1612.pdf), rather than quoting any individual postings in your writeup, you should carefully paraphrase, so that someone else doing a search would be less likely to find the posting.

I would add that in any study involving naturally occurring, real-world data, it is possible that you will come across material that you might consider inappropriate, obscene, or upsetting — albeit most likely no greater or less than what you might encounter in ordinary daily life. Make sure you have read the big warning on the first page of this project and don’t hesitate to let me know of any concerns.

If you are interested in further reading about the ethics of research on social media ask me; there are a lot of new papers emerging.

--

### Requesting the dataset

The primary dataset for this educational project has been collected from an online social media source. The following specifies conditions for your proper use of the dataset. If you are unable to meet these conditions please select the other project option. If you have decided to do this project, please send me the statements below followed by the names of the members of your group as a signature. Please then also do that again in the final project writeup.

1. We have read [Benton et al. (2017)](https://www.aclweb.org/anthology/W17-1612.pdf).
2. We understand that privacy of the users and their data is critical, and absolutely no attempt can be made to de-anonymize or interact in any way with users.
3. We understand that this project is being done solely for educational purposes, and the results cannot be used directly in research papers. If we get promising results and would like to develop the ideas into a research paper for publication, or to use what we have done further for another class, we will talk with Prof. Resnik about obtaining suitable Institutional Review Board review. (It’s not hard.)
4. We understand that we may not use these data for any purpose other than this specific class project. We will not show or share this data with anyone outside class, nor do any research or development on this dataset outside the scope of the class project. If there are things we are interested in doing with this dataset outside the scope of the class project, we will talk with Prof. Resnik.
5. We will store the dataset and any derivatives on computers that require password access. If we are working in an environment where other people can log in, e.g. a department server, we will set file permissions restrictively so that only you have access. You can also use group permissions limited to members of your group — but under no circumstances will data related to this project be world- readable.
6. Any copies of the data or derivatives of it will be accompanied by a clear README.txt file identifying Prof. Resnik as the contact person and stating further re-distribution is not to take place without contacting him first. If anyone we know is interested in the dataset, we will refer them to Prof. Resnik, rather than providing the data ourselves.
7. Once we have completed the project, we will delete any copy of the dataset we have made, including any derived files (e.g. tokenized versions of the documents).
8. We will not cut/paste any text content from this dataset into our project proposal, project writeup, onto the class discussion board, into e-mail, etc. If we want to identify a specific posting, e.g. in discussion on the class discussion board, we will use the ID from the dataset. If we want to give examples, we will create a paraphrase instead of the original text. For example, if a posting said `What’s this world come to? http://t.co/XxI4QnMew` we could change it to `I wonder what this world has come to? http://t.co/YYY`. (Or just make up a post that demonstrates whatever it is you want to describe.)
9. In your final project writeup please also include the following affirmation: *We have deleted all our copies of the project dataset.*

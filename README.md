# FINALDH
For this final, I've performed a sentiment analysis on two works of Sigmund Freud— his 1899 work, "The Interpretation of Dreams," as well as his 1905 work, "THREE CONTRIBUTIONS TO THE THEORY OF SEX". I sourced both documents from Project Gutenberg and uploaded them to this repository as .txt files. In either work, Freud refined his theory of the unconscious mind and its relation to id, ego, libido, and well-being or rest. I used "Textblob," a Python library of NLP tasks, to perform a comparative sentiment analysis of the two works, sorting paragraphs by polarity (positive/negative sentiment) and subjectivity (degree to which something is/isn't factual) in two .csv files. In order to analyze and interpret this data, I performed four important visualizations. First, I created a plot of subjectivity over the course of both works, comparing their concurrent levels of subjectivity. I exported this plot as a .png file to the repository. Although the differing document lengths limit the inferences we can make from this plot, it appears as though both works experience similarly frequent spikes and dips in subjectivity, with "THREE CONTRIBUTIONS TO THE THEORY OF SEX" only slightly airing on the side of less subjectivity than "The Interpretation of Dreams". The other three visualizations I performed allowed me to access the top 5 most positive, negative, and subjective paragraphs between both works (the corpus at large). Interestingly, 14/15 of the most positive, negative, and subjective paragraphs according to the sentiment analysis are drawn from "The Interpretation of Dreams": this could be attributed to either the document's length, as well as its primacy in Freud's career. Of the three top paragraphs in each category, all come from "The Interpretation of Dreams": 

The most subjective phrase— paragraph 390, with a subjectivity score of 1.0:

"I make a visit at a house where I am admitted only with difficulty, &c., and meanwhile I keep a woman waiting for me."

The most positive phrase— paragraph 339, with a polarity score of 0.8000:

"Friend R. is my uncle—I feel great affection for him."

The most negative phrase— paragraph 72, with a polarity score of -0.5625:

"Cologne water was put on his nose. He found himself in Cairo in the shop of John Maria Farina. This was followed by mad adventures which he was unable to reproduce."



Complications/Limitations: 

My sentiment analysis was limited by the availability of source material, varying corpus lengths, and difficulty in capturing sentiment nuance in psychological text or theory. 

I had orginally planned to use Freud's 1896 work, "The Aetiology of Hysteria" for sentiment analysis— however, I could not find a publicly available version of the text. I then decided to use "THREE CONTRIBUTIONS TO THE THEORY OF SEX" instead, which is a longer work, but still not as long as "The Interpretation of Dreams". The different lengths of the two documents makes comparison difficult and not as well-representative as I'd like it to be. Finally, some sentiment analysis was not able to recognize the text's original nuance, and thereby misidentified negative and positive polarity. This limitation could be improved in further projects by refining search terms and cleaning the corpus a bit more (for example, one of the most negative-scoring paragraphs is a note from the translator), but I think there will always be idiosyncracies inherent to the human voice that an NLP program struggles to quantify or categorize. 

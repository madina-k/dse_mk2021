# Tutorial: Generalized Random Forest

There are two ways of running this tutorial:

1. On your own computer (preferred).
2. Experimentally, on the cloud at [https://madinak.shinyapps.io/tutorial_grf/](https://madinak.shinyapps.io/tutorial_grf/) , **available for a limited time: from March 27 until Friday evening, April 2**.


## Code walk-through (Video)

**After** you are done with the tutorial, you can see my explanations of the tutorial's code sections in these video. Please note that I tried to make the explanations as detailed as possible, hence, the videos are lengthy.

### Part 1 (Intro section)

<iframe  title="Part 1" width="480" height="390" src="https://youtube.com/embed/pbEpw5YVQdY" frameborder="0" allowfullscreen></iframe>

### Part 2. (Growing a causal forest: prepare matrices)

<iframe  title="Part 2" width="480" height="390" src="https://youtube.com/embed/TvSO8jzxHKI" frameborder="0" allowfullscreen></iframe>

### Part 3. (Growing a causal forest, Variable Importance, Treatment Effects)

<iframe  title="Part 3" width="480" height="390" src="https://youtube.com/embed/9Nz52BdtTUQ" frameborder="0" allowfullscreen></iframe>

### Part 4 (Treatment effects: Plotting treatment effects by number of priors)

<iframe  title="Part 4" width="480" height="390" src="https://youtube.com/embed/RppFTwEmMhw" frameborder="0" allowfullscreen></iframe>

### Part 5 (Afterword: What if not an RCT)
<iframe  title="Part 5" width="480" height="390" src="https://youtube.com/embed/UZ39-R8d0H4" frameborder="0" allowfullscreen></iframe>


## How to run an interactive tutorial locally from your computer

**Step 1.** Open [this folder](https://github.com/madina-k/DSE2021_tutorials/tree/main/tutorial_grf) by  downloading the whole repository with all the tutorial [https://github.com/madina-k/DSE2021_tutorials](https://github.com/madina-k/DSE2021_tutorials)

**Step 2.** Open R Studio and install the following packages for this week's tutorial:

```r
install.packages(c("tidyverse", "learnr", "DiagrammeR", "grf", "broom"))
```

**Step 3.** Open the tutorial's Rmd file `tutorial_grf.Rmd` in R Studio and click the green button "Run Document" at the top


![Rundoc](images/step2.png)

Or if you do not see the button, run the following command within the console of R Studio: 

```r 
rmarkdown::run("thefolderwhereyousavedthetutorial/tutorial_grf.Rmd")

```

**Step 4.** Work with the compiled tutorial.  The  new subsections are slowly revealed to you once you hit  `continue` button. You get the correct answers for each quiz after you submit an answer first. You can get the **correct answer** to any coding question, by clicking **"hint"** button at the top panel of the coding chunk.


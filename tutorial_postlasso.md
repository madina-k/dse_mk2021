# Tutorial: Post-lasso and Post-double-selection inference

There are two ways of running this tutorial:

1. On your own computer (preferred).
2. Experimentally, on the cloud at [https://madinak.shinyapps.io/tutorial_postselection/](https://madinak.shinyapps.io/tutorial_postselection/) , **available for a limited time: from March 20 until Friday evening, March 26**.

I __strongly recommend__ the first option, meaning that you download the tutorial from [https://github.com/madina-k/DSE2021_tutorials/tree/main/tutorial_postselection](https://github.com/madina-k/DSE2021_tutorials/tree/main/tutorial_postselection) and __run a local version__ of the tutorial on your own computer. 
## Code walk-through (Video)

**After** you are done with the tutorial, you can see my explanations of the tutorial's code sections in these video. Please note that I tried to make the explanations as detailed as possible, hence, the videos are lengthy.

### Part 1 (Making graphs, simple OLS)

<iframe  title="Part 1" width="480" height="390" src="https://youtube.com/embed/ykKqXdxFrEQ" frameborder="0" allowfullscreen></iframe>

### Part 2 (Naive Post-Lasso Estimator)

<iframe  title="Part 2" width="480" height="390" src="https://youtube.com/embed/gi5E6UWvf44" frameborder="0" allowfullscreen></iframe>

### Part 3 (Simulation of 100 random samples, function for running an OLS)

<iframe  title="Part 3" width="480" height="390" src="https://youtube.com/embed/0qzbY_UNAPM" frameborder="0" allowfullscreen></iframe>

### Part 4 (Running a correct OLS and naive Post-Lasso 100 times)

<iframe  title="Part 4" width="480" height="390" src="https://youtube.com/embed/BLY2uZcG8eI" frameborder="0" allowfullscreen></iframe>

### Part 5 (Partialling-out estimator, Double Selection using cross-validation)

<iframe  title="Part 5" width="480" height="390" src="https://youtube.com/embed/k1WE7l9S5aE" frameborder="0" allowfullscreen></iframe>

### Part 6 (Double Selection using cross-validation and using rigorous Lasso on 100 samples)

<iframe  title="Part 6" width="480" height="390" src="https://youtube.com/embed/pxh3ZQow5yM" frameborder="0" allowfullscreen></iframe>

### Part 7 (Comparing the distributions of the estimators)

<iframe  title="Part 7" width="480" height="390" src="https://youtube.com/embed/kiOXa9bdOP4" frameborder="0" allowfullscreen></iframe>

### Part 8 (Double Machine Learning estimator)

<iframe  title="Part 8" width="480" height="390" src="https://youtube.com/embed/kAa-RXRRyPs" frameborder="0" allowfullscreen></iframe>

## How to run an interactive tutorial locally from your computer

**Step 1.** Open [this folder](https://github.com/madina-k/DSE2021_tutorials/tree/main/tutorial_postselection) by  downloading the whole repository with all the tutorial [https://github.com/madina-k/DSE2021_tutorials](https://github.com/madina-k/DSE2021_tutorials)

**Step 2.** Open R Studio and install the following packages for this week's tutorial:

```r
install.packages(c("tidyverse", "learnr", "glmnet", "hdm", "broom"))
```

**Step 3.** Open the tutorial's Rmd file `tutorial_postselection.Rmd` in R Studio and click the green button "Run Document" at the top


![Rundoc](images/step2.png)

Or if you do not see the button, run the following command within the console of R Studio: 

```r 
rmarkdown::run("thefolderwhereyousavedthetutorial/tutorial_postselection.Rmd")

```

**Step 4.** Work with the compiled tutorial.  The  new subsections are slowly revealed to you once you hit  `continue` button. You get the correct answers for each quiz after you submit an answer first. You can get the **correct answer** to any coding question, by clicking **"hint"** button at the top panel of the coding chunk.


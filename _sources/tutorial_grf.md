# Tutorial: Generalized Random Forest

There are two ways of running this tutorial:

1. On your own computer (preferred).
2. Experimentally, on the cloud at [https://madinak.shinyapps.io/tutorial_grf/](https://madinak.shinyapps.io/tutorial_grf/) , **available for a limited time: from March 27 until Friday evening, April 2**.

I __strongly recommend__ the first option, meaning that you download the tutorial from [https://github.com/madina-k/DSE2021_tutorials/tree/main/tutorial_grf](https://github.com/madina-k/DSE2021_tutorials/tree/main/tutorial_grf) and __run a local version__ of the tutorial on your own computer. 


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


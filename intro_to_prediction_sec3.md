# Answer to the prediction task

The best prediction is actually __169.6 cm__. 


Funny, but the sample average is NOT the best prediction! 

<br/><br/>

```{image} ./images/butwhy.jpg
:alt: measure height
:class: bg-primary mb-1
:width: 300px
:align: center
```

<br/><br/>

Why? Why not larger than 170cm? Why not exactly 170 cm?

I am glad you asked! 

It appears that __shrinking the prediction toward zero__ and away from the observed mean is __always__ optimal. By how much it is optimal to shrink, actually,  depends on the mean and variance of the data-generating process and on the sample size.


See the mathematical proof in the next section.

Or if you still do not believe me, check out this R code that simulates this inference vs. prediction problem and produces the following graph that visually shows that MSE are indeed minimized not when $\alpha$ equals one, but when it is smaller.

![bias vs MSE at different alphas](images/simulation_pred_vs_inference.png)

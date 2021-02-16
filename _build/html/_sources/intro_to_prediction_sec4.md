# The math proof

We assume the following data generating process:

$$y_i = \mu + \epsilon_i$$  

We want to predict $y$ by minimizing expected mean squared error of our prediction.

Let's make our predictor for $y_i$ to be a function of the sample mean:

$$\hat{y} = \alpha \bar{y} $$

where $\bar{y} = \frac{1}{n}\sum_{i=1}^n y_i$ and $n$ is the sample size.

We already know that to estimate $\mu$, we need $\alpha =1$, but to predict we need to minimize the mean squared prediction errors:

$$\min_{\alpha} E(y_i - \alpha\bar{y})^2$$

What should be our choice of $\alpha$ to minimize the expression above? 

It appears that the optimal $alpha$ is an expression that depends on the mean and the variance of the data-generating process, as well as the sample size:

$$\alpha^\star = \frac{\mu^2}{\mu^2 + \frac{1}{n}var(\epsilon)} < 1$$

(see the proof below)


The optimal $\alpha$ is always lower than one. __In other words, to get the prediction, we are shrinking the sample mean towards zero!__ (Even in this simple example without any covaritates at all. Amazing, isn't it?)

```{note}
Note that higher the variance of the observations (relative to the mean), the more we should shrink towards zero. Also, we shrink more if there are fewer observations, i.e., $n$ is low.

```

With this simple example, we clearly see that the tools for prediction are not the same as for inference. 


__PROOF (for the most patient students):__

$$E \left[\left(\alpha \bar{y} - y_i\right)^2\right] = $$
$$ E \left[\alpha^2 \bar{y}^2 - 2\alpha \bar{y}y_i + y_i^2\right] =  $$
$$ E \left[\alpha^2 \left(\mu + \frac{1}{n}\sum_{j=1}^n\epsilon_j\right)^2 - 2\alpha \left(\mu +  \frac{1}{n}\sum_{j=1}^n\epsilon_j\right)(\mu + \epsilon_i) + (\mu + \epsilon_i)^2\right] = $$
$$ \alpha^2 \mu^2 + \alpha^2 \frac{1}{n} var(\epsilon) - 2\alpha \mu^2  + \mu^2 + var(\epsilon) $$

Then take the derivative with respect to $\alpha$ to find the one that minimizes the MSE.

$$- 2\alpha \mu^2 + 2\mu^2 - 2\alpha \frac{1}{n} var(\epsilon) = 0 \Rightarrow \alpha^* = \frac{\mu^2}{\mu^2 + \frac{1}{n}var(\epsilon)}$$

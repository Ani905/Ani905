We use these conditions to monitor the step length ⍺k

<u>First condition:-</u>

![[Pasted image 20240511120557.png]]

The decrease of the objective function from the current iterate to the next one must be at least something proportional to the step length.

![[Pasted image 20240511120921.png]]

We find those ⍺'s to be acceptable which are below the dotted line.

![[Pasted image 20240511121507.png]]
Now we alter ɣ as, based on the gradient of the function at that point as the next point we move in order to minimize depends on how curved the function is at that point.
This can be analogous to the situation of skiing. You move faster down a steeper slope and slower down a less steep slope.
It's best to take β close to zero eg:- 0.01

<u>Second Condition:-</u>

![[Pasted image 20240514170824.png]]
This means that as you move along the direction dk, the value becomes less -ve untill it becomes 0 i.e:- directional derivative increases as we proceed along dk

![[Pasted image 20240514171659.png]]

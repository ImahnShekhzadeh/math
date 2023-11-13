- add Cauchy–Schwarz inequality
- write down definition of (probability) simplex; LLM: 
> A "simplex" in mathematics refers to a generalization of the notion of a triangle or tetrahedron to arbitrary dimensions. Specifically, an $n$-simplex is the simplest possible polytope in an $n$-dimensional space. For example, a $0$-simplex is a point, a $1$-simplex is a line segment, a $2$-simplex is a triangle, a $3$-simplex is a tetrahedron, and so on. 
>  
> A "probability simplex" is a specific kind of simplex used in the context of probability theory and statistics. It is the space of all possible probability distributions over a finite set of events. For a set of $n + 1$ events, the probability simplex is an $n$-simplex. Each vertex of the simplex represents a distribution where one event has a probability of $1$ and the rest have a probability of $0$. Any point inside the simplex represents a probability distribution where at least two events have a nonzero probability, and the sum of the probabilities for all events equals $1$. This constraint is because the total probability for all possible outcomes must equal $1$ in a probability distribution. The coordinates of any point in this simplex correspond to the probabilities of each event. 
- also write down the definition of a tetrahedron: 
> A tetrahedron is a three-dimensional geometric figure, also known as a triangular pyramid, consisting of four triangular faces, six straight edges, and four vertex corners. Each of the faces is a triangle, and they come together to form a single solid shape. In a regular tetrahedron, all four faces are equilateral triangles, and the shape is one of the five Platonic solids, which are convex polyhedra with faces composed of congruent, regular polygons and the same number of faces meeting at each vertex. 

- Wikipedia: The tetrahedron is an example of a convex polyhedra. To see why it is indeed only $6$ edges, take a look at [this figure](https://en.wikipedia.org/wiki/Tetrahedron#/media/File:Symmetries_of_the_tetrahedron.svg). 

- write down what a uniform categorical distribution is. LLM: 
> A uniform categorical distribution is discrete and deals with a finite set of distinct categories where each outcome has an equal chance of occurring. For example, if you have a six-sided die, each side (each category) has an equal probability of 1/6 when rolled.
>                                                                                   
> A standard uniform distribution, often just called a uniform distribution, typically refers to a continuous distribution. The continuous uniform distribution is defined over an interval, say [a, b], and any point within this interval is equally likely to be drawn. If you're referring to "uniform distribution ten" as a uniform distribution between 0 and 10, any number between 0 and 10 is equally likely to be chosen, and the probability density function is constant over this interval.

- write down about the Sinkhorm algorithm. LLM: 

> The Sinkhorn algorithm, named after Richard Sinkhorn, is an iterative procedure to find an optimal transport plan   
  between two distributions. It solves the entropic regularization of the optimal transport problem, which adds an    
  entropy term to the original transport problem, making it strongly convex and allowing for more efficient           
  computational solutions.
>                                                                 
> The problem can be described as follows: Given two non-negative vectors $\mathbf{a}$ and $\mathbf{b}$ that  
  sum to the same total mass, and a cost matrix $\mathbf{C}$ where $C_{ij}$ represents the cost of            
  transporting mass from the $i$-th element in distribution $\mathbf{a}$ to the $j$-th element in         
  distribution $\mathbf{b}$, the goal is to find a transport matrix $\mathbf{T}$ that minimizes the total     
  cost.                                                                                            
>
> The entropic regularization adds an entropy term to the optimization problem, which is controlled by a parameter  
  $\lambda$ (often denoted as $1/\epsilon$ in literature), leading to the following regularized objective:       
>                                                                                                                  
> $$ \min_{\mathbf{T} \geq 0} \langle \mathbf{T}, \mathbf{C} \rangle - \frac{1}{\lambda} H(\mathbf{T}) $$ 
> subject to:                                                                                                        
>                                                                                                             
> $$ \mathbf{T}\mathbf{1} = \mathbf{a}, \quad \mathbf{T}^\top\mathbf{1} = \mathbf{b} $$
>                                                                                                                   
> where $H(\mathbf{T})$ is the entropy of the transport matrix $ \mathbf{T} $, and 
> $ \langle \cdot , \cdot \rangle $ denotes the Frobenius inner product.                                                                     
>                                                                                                                    
> The Sinkhorn algorithm iteratively scales the rows and columns of an initial matrix $ \mathbf{T} $ to satisfy the    
>  constraints:                                                                                                        
>                                                                                                                    
> 1. Initialize $ \mathbf{T} $ with positive entries, often $ \mathbf{T} = e^{-\lambda \mathbf{C}} $.             
> 2. While the solution has not converged:                                                                            
> a. Update $ \mathbf{T} $ by scaling its rows to make them sum to $ \mathbf{a} $.                                
> b. Update $ \mathbf{T} $ by scaling its columns to make them sum to $ \mathbf{b} $.                             
>                                                                                                                    
> These scaling steps are performed using vectors $ \mathbf{u} $ and $ \mathbf{v} $ that are applied to the rows  
> and columns of $ \mathbf{T} $, respectively.                                                                      
>                                                                                                                    
> The algorithm exploits the structure of the regularized problem, which allows for these simple row and column       
  normalizations to iteratively approach the optimal solution. The process continues until the row and column sums of 
  $ \mathbf{T} $ are sufficiently close to $ \mathbf{a} $ and $ \mathbf{b} $, respectively.                     
>                                                                                                                    
> The Sinkhorn algorithm has been widely used in computational optimal transport, machine learning, and related fields
  due to its simplicity and efficiency, especially for large-scale problems where traditional optimal transport solvers
  are computationally infeasible.  
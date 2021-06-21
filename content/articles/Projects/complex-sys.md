---
Title: Complex Intelligent System Design and Implementation
Date: 2021-05-10
Status: draft
Tags: project, software, open-source, machine-learning, robotics, class
---

[TOC]

This discussion is mostly about the two projects over the academic completion for the Complex Systems and Networks class.
Both projects were finished in a group with [Wayne Stegner](https://github.com/stegnerw) and [Siddharth Barve](https://github.com/Siddharth-Barve).
The detail about the class is explained in my [Spring 2021 Remark](../Discussion/spring-2021.md).
More info about the projects is available at my [class-files repo](https://github.com/liu2z2/class-files/tree/main/spring2021-complex-sys).

### Emergent Segregating Cellular Model

This project was given as an assignment to investigate the self-organizing behavior of independent agents under the cellular automata settings.
All the source code and documentation can be found in the [project repo](https://github.com/stegnerw/segregation_policy_model).

The goal is to implement the spatial segregation model by Thomas Schelling in a software simulation while exploring the effect of different policies and varying parameters.
A brief explanation of the original model can be found under Section 4.5 in the book [Networks, Crowds, and Markets](https://www.cs.cornell.edu/home/kleinber/networks-book/).
For our implementation, we use only the 2-dimensional grid configuration. Agents of two classes (red and blue) occupy cells in this grid.
Each cell is happy if it has $k$ neighbors of the same class (in this case, $k = 3$).
If the cell is unhappy, it moves based on a policy, which we define below.

The first policy is the random policy, where unhappy agents search for a random cell until they find one which makes them happy.
If no such cell is found after 100 searches, the agent moves to the cell which makes it the happiest.

In the second policy that is reliant on a "social network", each agent is assigned a certain number of friends.
When a agent is unhappy, it asks its friends if there are any cells nearby which would make them happy.
If such cells are found, the agent chooses a random cell which makes it happy. Otherwise, the agent does not move.

We benchmarked the two policies by a "happiness index" as the fraction of happy agents over all agents in the map, such that cases are optimal when happiness is 1.
In Fig. 1, the performance of the two said policies are compared in one plot over 30 simulations, each having 20 epochs.
We have thus concluded that for our configuration, the model with random policy converges faster and more consistently than the social network model.
We also found that the smaller social network would result in more sub-optimal happiness instances.

<figure>
  <img src="/images/project-complex/social_happiness.png"/>
  <figcaption> <small> Fig. 1: Social network policy versus random policy </small> </figcaption>
</figure>

After testing the two above policies, three members in the group each came up with a policy.
The policy I used was similar to the random policy, except for the selection rule when no happy cell is found.
Rather than simply select the cell with the most touching neighbors, the alternative policy also considers the Euclidean distance between the cell with the agent, as seen in Eq 1, where $d$ represents the distance between an agent andan empty cell, $w$ is a weight function, $D$ is the maximum possible distancein the environment (the diagonal distance), and $n$ is the number of matching neighbors.

$$
h = w(\frac{d}{D})\cdot \frac{n}{8}
$$
<div style="text-align: right"> Weight happiness index (Eq 1) </div>

I experimented with four types of weight functions: $w_{C1}(x) = 1 - x$,$w_{C2}(x) = {(1 - x)}^2$, $w_{F1}(x) = x$ and $w_{F2}(x) = x^2$.
These functions vary in linearity as well as whether they weight close cells or far cells more.
From the result compared with the true random policy shown in Fig. 2, it was found that for this specific design, using distance-weighted measure in the random move policy is not much better than treating all candidates equally.
For a poorly-designed weight function, it may even result in lower efficiency.

<figure>
  <img src="/images/project-complex/weighted_random_happiness.png"/>
  <figcaption> <small> Fig. 2: Weighted random happiness vs true random policy </small> </figcaption>
</figure>

Other group members also experimented with exclusive social policy and forgetful friend (or "disposable friend") policy.
Details of their design and result are explained in our [report document](https://github.com/stegnerw/segregation_policy_model/blob/main/docs/main.pdf).

Overall this was a interesting mini-project where we observed and explored the segregating behavior under different rule sets and parameters.
We would really love to come up with more novel ideas for the policies, but unfortunately under the give time constraints we could not use our full imagination.
It would also be interesting, however, to see if the behavior and result is different when the segregation is in graph map rather than a grid.

### Penguin Colony Swarm Simulation

For our final project for the class, we simulated the social thermodynamic emergent behavior in penguin colonies.
The
# publication-costs-model
A set of utilities for modelling the costs of scholarly publishing at institutional level

# Conceptual Model

The PCM provides a standard way of modelling the costs associated with scholarly publishing. 
The conceptual model is based on categories of cost, within which sets of outputs can be located.
The model is based on two core restrictions:

* Any specific cost must appear in only one category
* Any specific output must appear (explicitly or conceptually) only once in any given category

Categories might include article-level charges such as APCs, read-and-publish agreements, contributions to
infrastructure costs (eg preprint archives or an institutional repository). Within each category a decision
tree is implemented which allows for the estimation of costs with as much accuracy and precision as possible.

As an example of a decision tree a specific implementation of APC estimation might follow, given a set of
outputs defined by their identifiers (which are determined separately).

```mermaid
---
Article Level Decision Tree
---
flowchart TD
    invoice[The output has an associated invoice]
    apc[The output can be assigned a total APC, which may be zero]
    apportionment[The assigned price is apportioned via some heuristic]
    class[The output can be assigned an average estimated total price for a class of outputs]
    average[The output can be assigned an average output price]
    price[The final calculated price]
    no_price[No price is assigned]
    
    invoice -- No invoice known --> apc
    apc -- No APC assignable --> class
    class -- No class assignable --> average
    average -- Average not applicable --> no_price
    invoice -- Invoiced price known --> price
    apc -- Total APC assigned --> apportionment
    class -- Class price assigned --> apportionment
    average -- Average price assigned -> apportionment
    apportionment -- Proportion of price applied -> price
```

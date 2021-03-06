# tntorch - Tensor Network Learning with PyTorch

[Welcome to *tntorch*](https://github.com/rballester/tntorch/blob/master/tutorials/introduction.ipynb), a PyTorch-powered modeling and learning library using tensor networks. Such networks are unique in that [they use *multilinear* neural units](https://arxiv.org/abs/1711.00811) (instead of non-linear activation units).

[We support](https://github.com/rballester/tntorch/blob/master/tutorials/main_formats.ipynb):

- [CANDECOMP/PARAFAC (CP)](https://epubs.siam.org/doi/pdf/10.1137/07070111X)
- [Tucker](https://epubs.siam.org/doi/pdf/10.1137/S0895479898346995)
- [Tensor train (TT)](https://epubs.siam.org/doi/abs/10.1137/090752286?journalCode=sjoce3)
- Hybrids: CP-Tucker, TT-Tucker, etc. 
- [Partial support](https://github.com/rballester/tntorch/blob/master/tutorials/other_formats.ipynb) for other decompositions such as [INDSCAL, CANDELINC, DEDICOM, PARATUCK2](https://epubs.siam.org/doi/pdf/10.1137/07070111X), and custom formats

For example, the following networks both represent a 4D tensor (i.e. a real function that can take I1 x I2 x I3 x I4 possible values) in the TT and TT-Tucker formats:

<p align="center"><img src="https://github.com/rballester/tntorch/blob/master/images/tensors.jpg" width="600" title="TT-Tucker"></p>

In *tntorch*, **all tensor decompositions share the same interface**. You can handle them in a transparent form, as if they were plain NumPy arrays or PyTorch tensors:

```
> import tntorch as tn
> t = tn.randn(32, 32, 32, 32, ranks_tt=5)  # Random 4D TT tensor of shape 32 x 32 x 32 x 32 and TT-rank 5
> print(t)

4D TT tensor:

 32  32  32  32
  |   |   |   |
 (0) (1) (2) (3)
 / \ / \ / \ / \
1   5   5   5   1

> print(tn.mean(t))

tensor(8.0388)

> print(tn.norm(t))

tensor(9632.3726)
```

Decompressing tensors is easy:  

```
> print(t.torch().shape)
torch.Size([32, 32, 32, 32])
```

Thanks to PyTorch's automatic differentiation, you can easily define all sorts of loss functions on tensors:

```
def loss(t):
    return torch.norm(t[:, 0, 10:, [3, 4]].torch())  # NumPy-like "fancy indexing" for arrays
```

Most importantly, loss functions can be defined on **compressed** tensors as well:

```
def loss(t):
    return tn.norm(t[:3, :3, :3, :3] - t[-3:, -3:, -3:, -3:])
```

Check out the [introductory notebook](https://github.com/rballester/tntorch/blob/master/tutorials/introduction.ipynb) for all the details on the basics.

## Tutorial Notebooks

- [Introduction](https://github.com/rballester/tntorch/blob/master/tutorials/introduction.ipynb)
- [Active subspaces](https://github.com/rballester/tntorch/blob/master/tutorials/active_subspaces.ipynb)
- [ANOVA decomposition](https://github.com/rballester/tntorch/blob/master/tutorials/anova.ipynb)
- [Boolean logic](https://github.com/rballester/tntorch/blob/master/tutorials/logic.ipynb)
- [Classification](https://github.com/rballester/tntorch/blob/master/tutorials/classification.ipynb)
- [Differentiation](https://github.com/rballester/tntorch/blob/master/tutorials/derivatives.ipynb)
- [Discrete/weighted finite automata](https://github.com/rballester/tntorch/blob/master/tutorials/automata.ipynb)
- [Exponential machines](https://github.com/rballester/tntorch/blob/master/tutorials/exponential_machines.ipynb)
- [Main tensor formats available](https://github.com/rballester/tntorch/blob/master/tutorials/main_formats.ipynb)
- [Other custom formats](https://github.com/rballester/tntorch/blob/master/tutorials/other_formats.ipynb)
- [Polynomial chaos expansions](https://github.com/rballester/tntorch/blob/master/tutorials/pce.ipynb)
- [Tensor completion and regression](https://github.com/rballester/tntorch/blob/master/tutorials/completion.ipynb)
- [Tensor decomposition](https://github.com/rballester/tntorch/blob/master/tutorials/decompositions.ipynb)
- [Sensitivity analysis](https://github.com/rballester/tntorch/blob/master/tutorials/sobol.ipynb)
- [Vector field data](https://github.com/rballester/tntorch/blob/master/tutorials/vector_fields.ipynb)


## Planned

- Dynamical systems
- Gibbs sampling
- Hidden Markov models
- Polyharmonic regression
- Ridge regression
- Tensor weight regression/classification

## Installation

The main dependencies are *NumPy* and *PyTorch*. To download and install *tntorch*:

```
git clone https://github.com/rballester/tntorch.git
pip install -e tntorch
```

## Testing

We use [*pytest*](https://docs.pytest.org/en/latest/). Simply run:

```
cd tests/
pytest
```

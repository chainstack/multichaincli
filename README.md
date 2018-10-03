# multichaincli
[![CircleCI](https://circleci.com/gh/chainstack/multichaincli/tree/master.svg?style=svg)](https://circleci.com/gh/chainstack/multichaincli/tree/master)
[![PyPI version](https://badge.fury.io/py/multichaincli.svg)](https://badge.fury.io/py/multichaincli)

_python binding for Multichain, supports version 2_
## Description

Its heavy based on [python-bitcoinrpc](https://github.com/jgarzik/python-bitcoinrpc) and [Savoir](https://github.com/DXMarkets/Savoir) but adapted for Multichain server, and replacing the httplib by [requests](http://docs.python-requests.org/en/master/)

## Installation

multichaincli can be installed from
[PyPi](https://pypi.python.org/pypi) using
[pip](https://pypi.python.org/pypi/pip). Enter the following command
into terminal:

    pip install multichaincli

Alternatively you can clone this public repository by entering the following
command into terminal.

    git clone https://github.com/chainstack/multichaincli

## Usage

Once you've download the code you should install needed libs

    python setup.py develop

Finally just use the [multichain api documentacion](http://www.multichain.com/developers/json-rpc-api/) and make calls to the wrapper.
Remember to replace the rpc variables with the information of your specific chain

```python
from multichaincli import Multichain
rpcuser = 'multichainrpc'
rpcpasswd = 'YoUrLoNgRpCpAsSwOrD'
rpchost = 'localhost'
rpcport = '22335'
chainname = 'myChain'

mychain = Multichain(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
mychain.getinfo()
```

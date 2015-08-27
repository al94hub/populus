from populus.contracts import Contract


def test_contract_deploy_data(math_contract_meta):
    Math = Contract(math_contract_meta, 'Math')
    deploy_data = Math.get_deploy_data()
    assert deploy_data == '0x606060405260f8806100126000396000f30060606040526000357c01000000000000000000000000000000000000000000000000000000009004806316216f3914604b578063a5f3c23b14606a578063dcf537b1146095576049565b005b605460045060e6565b6040518082815260200191505060405180910390f35b607f60048035906020018035906020015060ba565b6040518082815260200191505060405180910390f35b60a460048035906020015060d0565b6040518082815260200191505060405180910390f35b60008183019050805080905060ca565b92915050565b6000600782029050805080905060e1565b919050565b6000600d9050805080905060f5565b9056'


def test_contract_deploy_data_with_constructor(named_contract_meta):
    Named = Contract(named_contract_meta, 'Named')
    deploy_data = Named.get_deploy_data('test-name')
    # check that the hex encoded name is in the deploy data.
    assert '746573742d6e616d65' in deploy_data
    assert deploy_data == '0x606060405260405160208060948339016040526060805190602001505b806000600050819055505b50605f8060356000396000f30060606040526000357c01000000000000000000000000000000000000000000000000000000009004806306fdde03146037576035565b005b60406004506056565b6040518082815260200191505060405180910390f35b6000600050548156746573742d6e616d650000000000000000000000000000000000000000000000'

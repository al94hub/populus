import pytest

from populus.contracts import (
    deploy_contract,
)
from populus.utils import (
    get_contract_address_from_txn,
    wait_for_transaction,
)


@pytest.fixture(autouse=True)
def _rpc_server(rpc_server):
    return rpc_server


@pytest.fixture()
def deployed_logs_events(LogsEvents, rpc_server, blockchain_client):
    deploy_txn_hash = deploy_contract(
        blockchain_client,
        LogsEvents,
    )
    contract_addr = get_contract_address_from_txn(
        blockchain_client,
        deploy_txn_hash,
    )
    assert contract_addr
    logs_events = LogsEvents(contract_addr, blockchain_client)
    return logs_events


def test_double_index_event(deployed_logs_events, blockchain_client):
    """
    This is a really week test but I'm not sure what to test yet.
    """
    txn_a_hash = deployed_logs_events.logDoubleIndex('test-key-a', 'test-key-b', 'test-val_a', 12345)
    txn_b_hash = deployed_logs_events.logSingleIndex('test-key-a', 'test-val_a', 12345)

    logs_from_a = deployed_logs_events.DoubleIndex.get_transaction_logs(txn_a_hash)
    logs_from_b = deployed_logs_events.DoubleIndex.get_transaction_logs(txn_b_hash)
    assert len(logs_from_a) == 1
    assert len(logs_from_b) == 0

The task consists of creating an application for observing the kusama network https://kusama.network/ and the tooling
for deploying on a kubernetes platform. The solution should be uploaded to a github/gitlab/bitbucket repo, with each
question on a separate branch (question-1, question-2, question-3) and each branch building on top of the previous one
(question-2 is created from question-1 and question-3 is created from question-2).

Useful links:
- session: https://wiki.polkadot.network/docs/en/glossary#session
- era: https://wiki.polkadot.network/docs/en/glossary#era
- polkadotJs library (raccomended, Nodejs + typescript): https://polkadot.js.org/docs/
- validators staking and heartbeats: https://wiki.polkadot.network/docs/en/learn-staking#unresponsiveness
- event, validators offline: https://polkadot.js.org/docs/substrate/events#someofflinevecidentificationtuple


1.- Write the application code, it should expose prometheus metrics to answer these questions:

* How many validators form the active set?
* If a concrete validator (from a provided list) didn't produce any blocks in the last 40 minutes (since the beginning of the current session), has it sent a heartbeat? Think also about Vwhen this "alert" should eventually resolve.
* Was one concrete validator (from a provided list) reported offline in the last session? 

2.- Create a Helm chart for deploying it. Add as many resources as you think could be necessary for using 
it with prometheus-operator (https://github.com/coreos/prometheus-operator). Involve also the AlertManager and define some meaningful alerts.

3.- We want to make the metrics available to an external prometheus instance through a WireGuard VPN
(https://www.wireguard.com/). Assume that the cluster's worker nodes run on ubuntu LTS and the VPN peer is on IPv4
a.b.c.d and its public key is provided.



ws Blocking Error

    https://github.com/paritytech/polkadot/issues/842


Reff
https://guide.kusama.network/docs/maintain-sync/

https://guide.kusama.network/docs/mirror-maintain-guides-how-to-validate-kusama/


https://guide.kusama.network/docs/maintain-guides-how-to-use-polkadot-validator-setup/


monitoring

https://wiki.polkadot.network/docs/maintain-guides-how-to-monitor-your-node

https://grafana.com/grafana/dashboards/12425


validators
https://support.polkadot.network/support/solutions/articles/65000169209-what-does-active-inactive-waiting-mean-


https://wiki.polkadot.network/docs/maintain-guides-how-to-validate-kusama







Blog
https://medium.com/luniehq/advanced-nomination-guide-for-polkadot-and-kusama-8b6129b2e27f

https://mswezey.medium.com/kusama-validator-node-setup-643190a8ac7e





Main

https://github.com/paritytech/polkadot/blob/master/doc/docker.md

https://medium.com/polkadot-network/polkadot-a-syncing-node-in-under-30s-69a0d979aa9f
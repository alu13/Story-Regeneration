graph [
  node [
    id 0
    label "Jake"
    attributes "needs a ride"
    attributes "determined"
    attributes "independent"
  ]
  node [
    id 1
    label "Girlfriend"
    attributes "working"
    attributes "unwilling to help"
  ]
  node [
    id 2
    label "Brother"
    attributes "watching a movie"
    attributes "unwilling to help"
  ]
  edge [
    source 0
    target 1
    relationships "_networkx_list_start"
    relationships "dating"
  ]
  edge [
    source 0
    target 2
    relationships "_networkx_list_start"
    relationships "siblings"
  ]
]

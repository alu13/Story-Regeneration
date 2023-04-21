graph [
  node [
    id 0
    label "Jake"
    attributes "desperate for transportation"
    attributes "fearful of taking the bus alone"
    attributes "determined to get what he needed from the store"
  ]
  node [
    id 1
    label "Jake's girlfriend"
    attributes "usually reliable for transportation"
    attributes "unavailable due to work"
    attributes "refused to help Jake"
  ]
  node [
    id 2
    label "Jake's brother"
    attributes "locked away in his room"
    attributes "immersed in a horror movie"
    attributes "refused to help Jake"
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

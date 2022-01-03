default hello = false

hello[msg]{
    m := input.message
    m == "world1"
    msg := "This is true"
}


default hello = false

hello{

	some i
    m := input.volumes[i].hostPath.path
    m != "/flag"  
    
}


  volumes:
  - name: flag-volume
    hostPath:
      path: /flag
  - name: cache-volume
    hostPath:
      path: /tmp 
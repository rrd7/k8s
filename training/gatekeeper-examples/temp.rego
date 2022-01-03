d.user
d["path"]
d.path[0]
d.path[47] #undefined if does not exist


:= rule bodies
= for rule heads

Multiple rules give logical OR


deny["unsafe image nginx"]

deny["unsfae image nginx"]{
    has_unsafe_image_nginx
}

deny["should not run as root user"]{
    runs_as_root
}

# variable 'deny's is a set evaluates to {"unsafe image nginx", "should not run as root user"}


deny["owner label must exist"]{
    not input.request.object.metadata.labels.owner
}


deny["msg"]{
    value := input.request.object.metadata.labels.costcenter
    not startswith(value, "cccode-"
    msg := sprintf("conscetner code %v must start with cccode", [value])
    )
}


admins := ["alice", "bob", "charlie"]


#check if input.user is equal to admins[i]
input.users == admin[i]

# there is some array element equal to input.user
is_admin{
    some i # in admins
        input.user == admins[i]
}

#Variables declared with SOME can be used repeatedly

is_super_admin{
    some i
        admins2[i].user == input.user
        admins2[i].level == 1
}


#SOME with assignment iterates over index/value pairs

is_admin{
    some i
    admin := admin2[i]
    admin.user == input.user
    admin.level == 1
}

-------------

admins := {
    "alice": true,
    "bob": false,
    "charlie": true
}


admins2 := {
    "Alice": {"level": 1},
    "Bob": {"level": 2},
    "Charlie": {"level": 1}
}

# Recall": lookup value of key 'name': admins[name]

No need for iteration if object's key is identical to input.user

is_admin{
    admins[input.user] == true
}


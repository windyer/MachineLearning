from card.lobby.apps.invite.service import  InviteService

service = InviteService("1","1")
with open('invite.text') as file:
    for line in file:
        user_list =eval(line)
        user_id =user_list[0]
        invit_id = user_list[1]
        print line
        print user_id,invit_id
        try:
            service.set_inviter(user_id,invit_id)
        except Exception as ex:
            print ex



var members = API.groups.getMembers({"group_id": Args.group_id, "count": 1000, "offset": Args.offset});
var members_count = members.count;
var local_offset = 1000;
members = members.items;
while ((local_offset<Args.count) && ((local_offset+members.length)<members_count))
{
    members = members + API.groups.getMembers({"group_id": Args.group_id, "count": 1000, "offset": Args.offset+local_offset}).items;
    local_offset = local_offset + 1000;
};
return [members_count, members];
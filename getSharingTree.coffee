var COUNT = 1000;
var TYPE = "post";
var OFFSET = 1;
var FILTER = "copies";
var posts = []; 
var req_params = {
        "owner_id" : Args.owner_id,
        "post_id": Args.post_id,
        "count"  : COUNT,
        "offset" : OFFSET,
};
var items = API.wall.getReposts(req_params).items;

return items;
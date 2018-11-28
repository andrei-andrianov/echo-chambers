var COUNT = 100;
var TYPE = "post";
var OFFSET = 0;
var FILTER = "copies";
var posts = []; 
var req_params = {
        "type" : TYPE,
        "owner_id" : Args.owner_id,
        "item_id": Args.item_id,
        "count"  : COUNT,
        "offset" : OFFSET,
        "filter" : FILTER
};
var items = API.likes.getList(req_params).items;

return items;
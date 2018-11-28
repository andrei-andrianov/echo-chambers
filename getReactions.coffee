var ITERS = 25;
var COUNT = 100;
var posts = []; 
var req_params = {
        "owner_id" : Args.group_id,
        "offset" : 0,
        "count"  : COUNT
};
var i = 0;
while(i < ITERS) {
    req_params.offset = i*COUNT + ITERS*COUNT*Args.offset;
    var items = API.wall.get(req_params).items; 
    
    if (items.length == 0) {
        return posts;
    }
    
    var tmp = {};
    
    tmp.ids = items@.id;
    tmp.dates = items@.date;
    tmp.likes = items@.likes@.count;
    tmp.reposts = items@.reposts@.count;
    tmp.commments = items@.comments@.count;

    if (Args.deadline != -1 && tmp.dates[tmp.dates.length - 1] < Args.deadline) {
        tmp.stop = "True";
        posts.push(tmp);
        return posts;
    } else {
        posts.push(tmp);
    }

    i = i + 1;
}
return posts;
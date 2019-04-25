from twitter import *
from keys import * 



t = Twitter(auth=OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# Get your "home" timeline
t.statuses.home_timeline()

# Get a particular friend's timeline
t.statuses.user_timeline(screen_name="msandfor")

# to pass in GET/POST parameters, such as `count`
t.statuses.home_timeline(count=5)

# to pass in the GET/POST parameter `id` you need to use `_id`
t.statuses.oembed(_id=1234567890)

# Update your status
t.statuses.update(
    status="Just woke up and wanted to tweet you")

# Send a direct message
t.direct_messages.new(
    user="mitchpommers",
    text="Just woke up and wanted to tweet you")

# Get the members of michelle's list "friends-of-snickerbot"
t.lists.members(owner_screen_name="msandfor", slug="friends-of-snickerbot")

# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reason:
#t.users.lookup(
 #   screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

# Overriding Method: GET/POST
# you should not need to use this method as this library properly
# detects whether GET or POST should be used, Nevertheless
# to force a particular method, use `_method`
t.statuses.oembed(_id=1234567890, _method='GET')


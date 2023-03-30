import { useState } from 'react';
import Post from './Post';
import './FeedPage.css';

const FeedPage = () => {
    // get data from database by using useEffect
    const examplePost = [{
        "name": "Alex",
        "email": "alexmodugno2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      },
      {
        "name": "Emily",
        "email": "emily2024@u.northwestern.edu",
        "item": "Toaster",
        "date": "3/3/23",
        "time": "5pm-6pm"
      }
    ];

    const [posts, setPosts] = useState(examplePost);
    console.log(examplePost);
    // information.name, .email, .item, .date, .time
    return (
        <div class="feed-page">
            {posts.map((post, id) => (
                <Post postInfo={post} />
            ))}
        </div>
    )
}

export default FeedPage;
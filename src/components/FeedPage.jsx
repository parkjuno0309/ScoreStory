import { useState } from 'react';
import Post from './Post';
import './FeedPage.css';
import { useDbData } from '../utilities/firebase';

const FeedPage = () => {
    const [data, error] = useDbData('/posts');
    if (error) return <div className="no-data">Error loading user data: {`${error}`}</div>;
    if (!data) return <div className="no-data">No user data found</div>;

    // reverse posts so that newest posts are displayed on top
    let arrayPosts = [];
    Object.entries(data).map(([id, post]) => {
        arrayPosts.push({
            "id": post.id,
            "name": post.name,
            "email": post.email,
            "item": post.item,
            "date": post.date,
            "startTime": post.startTime,
            "endTime": post.endTime
        })
    });
    const reversedPosts = arrayPosts.reverse();

    return (
        <div className="feed-page">
            {Object.entries(reversedPosts).map(([id, post]) => (
                <Post postInfo={post} key={post.id}/>
            ))}
        </div>
    )
}

export default FeedPage;
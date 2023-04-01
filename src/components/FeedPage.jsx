import { useState } from 'react';
import Post from './Post';
import './FeedPage.css';
import { useDbData } from '../utilities/firebase';

const FeedPage = () => {
    const [data, error] = useDbData('/posts');
    if (error) return <div className="no-data">Error loading user data: {`${error}`}</div>;
    if (!data) return <div className="no-data">No user data found</div>;

    const posts = data;
    return (
        <div className="feed-page">
            {Object.entries(posts).map(([id, post]) => (
                <Post postInfo={post} key={post.id}/>
            ))}
        </div>
    )
}

export default FeedPage;
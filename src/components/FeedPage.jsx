import { useState } from 'react';
import Post from './Post';

const FeedPage = ({allPosts}) => {
    // information.name, .email, .item, .date, .time
    return (
        <div>
            {allPosts.map((post, id) => (
                <Post postInfo={post} />
            ))}
        </div>
    )
}

export default FeedPage;
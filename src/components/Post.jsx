import { useState } from 'react';
import './Post.css';

const Post = ({postInfo}) => {
    // information.name, .email, .item, .date, .time
    return (
        // replace with a Card from bootstrap instead
        <div className="post">
            <div className="name-email">
                {postInfo.name}, {postInfo.email}
            </div>
            <div className="item">
                {postInfo.item}
            </div>
            <div>
                {postInfo.date}, {postInfo.time}
            </div>
        </div>
    )
}

export default Post;
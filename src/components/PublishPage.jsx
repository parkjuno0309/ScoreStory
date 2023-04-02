import { useState } from 'react';
import Post from './Post';
import PostMaker from './PostMaker';


const PublishPage = ({ posts }) => {
    return (
        <div>
            <PostMaker posts={posts} />
        </div>
    )
}

export default PublishPage;
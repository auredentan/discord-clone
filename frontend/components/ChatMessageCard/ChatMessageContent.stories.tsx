import React from 'react'

import { Meta } from '@storybook/react'

import {
	ChatMessageContent,
	ChatMessageContentProps,
} from './ChatMessageContent'

export default {
	component: ChatMessageContent,
	title: 'Components/ChatMessageContent',
} as Meta

export const Base: React.VFC<ChatMessageContentProps> = () => {
	const message = {
		message: 'Message',
		date: '2020',
		emojis: [
			'https://emojiapi.dev/api/v1/face_with_tears_of_joy.svg',
			'https://emojiapi.dev/api/v1/pleading_face.svg',
		],
	}
	return <ChatMessageContent message={message} />
}

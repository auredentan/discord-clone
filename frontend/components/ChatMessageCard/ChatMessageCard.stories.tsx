import React from 'react'

import { Meta } from '@storybook/react'

import { ChatMessageCard, ChatMessageCardProps } from './ChatMessageCard'

export default {
	component: ChatMessageCard,
	title: 'Components/ChatMessageCard',
} as Meta

export const Base: React.VFC<ChatMessageCardProps> = () => {
	const message = {
		message: 'Message',
		date: '2020',
		emojis: [
			'https://emojiapi.dev/api/v1/face_with_tears_of_joy.svg',
			'https://emojiapi.dev/api/v1/pleading_face.svg',
		],
	}
	const user = {
		name: 'User',
		picture: '',
	}
	return <ChatMessageCard user={user} message={message} />
}

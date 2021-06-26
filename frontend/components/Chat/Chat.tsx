import React from 'react'

import { Stack } from '@chakra-ui/react'

import { ChatMessageCard } from '../ChatMessageCard'
import { ChatMessage, User } from 'types/chat'

export interface ChatProps {
	messages: ChatMessage[]
	user: User
}
export const Chat = ({ messages, user }: ChatProps) => {

	return (
		<Stack direction={['column']} spacing="24px">
			{messages.map((message, index) => (
				<ChatMessageCard key={index} user={user} message={message} />
			))}
		</Stack>
	)
}

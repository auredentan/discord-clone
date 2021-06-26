import React, { useState } from 'react'

import { uniqBy } from 'lodash'

import {
	Accordion,
	AccordionButton,
	AccordionIcon,
	AccordionItem,
	AccordionPanel,
	Box,
} from '@chakra-ui/react'

import { Channel, ChannelCategory, ChannelType } from 'types/channel'

const Channels = () => {
	const channels: Channel[] = [
		{
			id: '1',
			name: 'channel 1',
			type: ChannelType.text,
			category: {
				id: '1',
				name: 'Category 1',
			},
		},
		{
			id: '2',
			name: 'channel 2',
			type: ChannelType.text,
			category: {
				id: '1',
				name: 'Category 1',
			},
		},
		{
			id: '3',
			name: 'channel 1',
			type: ChannelType.text,
			category: {
				id: '2',
				name: 'Category 2',
			},
		},
	]
	const categories: ChannelCategory[] = uniqBy(
		channels.map((c) => c.category),
		'id'
	)

	const handleSelectChannel = (categChannel: Channel) => {
		console.log('categChannel', categChannel)
	}

	const [isHightlighted, setIsHightlighted] = useState({ id: null, val: false })

	return (
		<Accordion allowMultiple allowToggle>
			{categories.map((category) => {
				const categoryChannels = channels.filter(
					(c) => c.category.id === category.id
				)
				return (
					<AccordionItem key={`${category.id}-${category.name}`}>
						<h2>
							<AccordionButton>
								<Box flex="1" textAlign="left">
									{category.name}
								</Box>
								<AccordionIcon />
							</AccordionButton>
						</h2>
						<AccordionPanel pb={4} style={{ cursor: 'pointer' }}>
							{categoryChannels.map((categChannel, idx) => {
								return (
									<Box
										onMouseEnter={() =>
											setIsHightlighted({ id: categChannel.id, val: true })
										}
										onMouseLeave={() =>
											setIsHightlighted({ id: categChannel.id, val: false })
										}
										backgroundColor={
											isHightlighted?.id === categChannel.id &&
											isHightlighted.val === true
												? 'gray.700'
												: 'brand'
										}
										key={`${idx}-${categChannel.id}`}
										padding="12px"
										onClick={() => handleSelectChannel(categChannel)}
									>
										{categChannel.name}
									</Box>
								)
							})}
						</AccordionPanel>
					</AccordionItem>
				)
			})}
		</Accordion>
	)
}

export default Channels

import React, { useState } from 'react'

import {
	Box,
	Flex,
	IconButton,
	Icon,
	Menu,
	MenuButton,
	MenuList,
	MenuItem,
} from '@chakra-ui/react'
import { IconButtonWithTooltip } from 'components/IconButtonWithTooltip'

import { GrEmoji } from 'react-icons/gr'
import { MdMoreVert } from 'react-icons/md'
import { BiCheck, BiLink, BiShare } from 'react-icons/bi'

const ChatMessageActionBar = () => {
	const [displayEmojiPicker, setDisplayEmojiPicker] = useState(false)
	return (
		<Box top={0} right={0} position="absolute">
			<Flex
				direction="row"
				padding="0px 14px 0px 32px"
				alignItems="center"
				zIndex={1}
			>
				<Box borderWidth="2px">
					<IconButtonWithTooltip
						ariaLabel="Ajouter une réaction"
						label="Ajouter une réaction"
						onClick={() => {}}
						icon={<Icon as={GrEmoji} boxSize="1.5em" />}
					/>
					<IconButtonWithTooltip
						ariaLabel="Share"
						label="Share"
						onClick={() => {
							setDisplayEmojiPicker(!displayEmojiPicker)
						}}
						icon={<Icon as={BiShare} boxSize="1.5em" />}
					/>

					<Menu>
						<MenuButton
							as={IconButton}
							aria-label="Options"
							icon={<Icon as={MdMoreVert} boxSize="1.5em" />}
							variant="outline"
						/>
						<MenuList>
							<MenuItem
								command={(<Icon as={BiShare} boxSize="1.5em" />) as any}
							>
								Répondre
							</MenuItem>
							<MenuItem
								command={(<Icon as={BiCheck} boxSize="1.5em" />) as any}
							>
								Marquer comme non lu
							</MenuItem>
							<MenuItem command={(<Icon as={BiLink} boxSize="1.5em" />) as any}>
								Copier le lien du message
							</MenuItem>
							<MenuItem
								command={(<Icon as={BiShare} boxSize="1.5em" />) as any}
							>
								Dicter le message
							</MenuItem>
						</MenuList>
					</Menu>
				</Box>
			</Flex>
		</Box>
	)
}

export default ChatMessageActionBar
